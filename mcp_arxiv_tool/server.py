"""MCP server for Benty Fields ArXiv daily papers."""
import asyncio
import json
import logging
from pathlib import Path
from typing import Any, Sequence
from datetime import datetime

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from benty_client import BentyFieldsClient
from pdf_processor import PDFProcessor

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize server
app = Server("benty-fields-arxiv")

# Global client and processor (initialized on first use)
_client: BentyFieldsClient | None = None
_processor: PDFProcessor | None = None
_config: dict | None = None


def load_config() -> dict:
    """Load configuration from config.json."""
    global _config
    if _config is not None:
        return _config
    
    config_path = Path(__file__).parent / "config.json"
    if not config_path.exists():
        raise FileNotFoundError(
            f"config.json not found at {config_path}. "
            "Please create it with your benty-fields credentials."
        )
    
    with open(config_path, "r") as f:
        _config = json.load(f)
    
    return _config


def get_client() -> BentyFieldsClient:
    """Get or create BentyFieldsClient instance."""
    global _client
    if _client is None:
        config = load_config()
        benty_config = config.get("benty_fields", {})
        email = benty_config.get("email", "")
        password = benty_config.get("password", "")
        
        if not email or not password:
            raise ValueError(
                "benty_fields.email and benty_fields.password must be set in config.json"
            )
        
        _client = BentyFieldsClient(email, password)
        _client.login()
    
    return _client


def get_processor() -> PDFProcessor:
    """Get or create PDFProcessor instance."""
    global _processor
    if _processor is None:
        config = load_config()
        tmp_dir = config.get("tmp_dir")
        if tmp_dir:
            tmp_dir = Path(tmp_dir)
        _processor = PDFProcessor(tmp_dir=tmp_dir)
    
    return _processor


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="fetch_daily_papers",
            description="Fetch top N papers for a given date from benty-fields.com. "
                       "Returns paper metadata including title, authors, abstract, and links. "
                       "If no papers are found for the date, returns a message indicating no updates.",
            inputSchema={
                "type": "object",
                "properties": {
                    "date": {
                        "type": ["string", "null"],
                        "description": "Date in YYYY-MM-DD format. If not provided, uses value from config.json. If config.json has null, uses today's date.",
                        "format": "date"
                    },
                    "num_papers": {
                        "type": "integer",
                        "description": "Number of top papers to fetch. If not provided, uses value from config.json (default: 10).",
                        "minimum": 1,
                        "maximum": 100
                    }
                }
            }
        ),
        Tool(
            name="download_paper_pdf",
            description="Download PDF for a specific paper. Returns the path to the downloaded PDF.",
            inputSchema={
                "type": "object",
                "properties": {
                    "arxiv_id": {
                        "type": "string",
                        "description": "ArXiv ID of the paper (e.g., '2601.04344')"
                    },
                    "pdf_url": {
                        "type": "string",
                        "description": "URL of the PDF to download"
                    }
                },
                "required": ["pdf_url"]
            }
        ),
        Tool(
            name="extract_pdf_text",
            description="Extract text from a downloaded PDF file.",
            inputSchema={
                "type": "object",
                "properties": {
                    "pdf_path": {
                        "type": "string",
                        "description": "Path to the PDF file"
                    }
                },
                "required": ["pdf_path"]
            }
        ),
        Tool(
            name="convert_pdf_to_markdown",
            description="Convert a PDF file to Markdown format. Better for AI analysis than plain text extraction.",
            inputSchema={
                "type": "object",
                "properties": {
                    "pdf_path": {
                        "type": "string",
                        "description": "Path to the PDF file"
                    },
                    "save_to_file": {
                        "type": "boolean",
                        "description": "Whether to save Markdown to a file. If true, saves to same location as PDF with .md extension.",
                        "default": False
                    }
                },
                "required": ["pdf_path"]
            }
        ),
        Tool(
            name="generate_daily_summary",
            description="Generate a markdown summary document from processed papers. "
                       "Includes paper metadata and PDF content (converted to Markdown) for AI analysis.",
            inputSchema={
                "type": "object",
                "properties": {
                    "papers": {
                        "type": "array",
                        "description": "Array of paper dictionaries with metadata",
                        "items": {
                            "type": "object"
                        }
                    },
                    "output_path": {
                        "type": "string",
                        "description": "Path where the summary markdown file should be saved"
                    },
                    "include_pdf_text": {
                        "type": "boolean",
                        "description": "Whether to include PDF content in the summary",
                        "default": True
                    },
                    "use_markdown": {
                        "type": "boolean",
                        "description": "Whether to convert PDF to Markdown format (better for AI analysis). If false, uses plain text extraction.",
                        "default": True
                    }
                },
                "required": ["papers", "output_path"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> Sequence[TextContent]:
    """Handle tool calls."""
    try:
        if name == "fetch_daily_papers":
            # Get date from arguments, config, or use today
            date = arguments.get("date")
            if date is None:
                config = load_config()
                date = config.get("date")
                if date is None:
                    date = datetime.now().strftime("%Y-%m-%d")
                # Handle numeric date format (e.g., 20260109)
                elif isinstance(date, int):
                    date_str = str(date)
                    if len(date_str) == 8:
                        date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
            
            # Get num_papers from arguments or config
            num_papers = arguments.get("num_papers")
            if num_papers is None:
                config = load_config()
                num_papers = config.get("num_papers", 10)
            
            client = get_client()
            papers = client.fetch_daily_papers(date, num_papers=num_papers)
            
            # Check if no papers found
            if len(papers) == 0:
                result = {
                    "date": date,
                    "num_papers_requested": num_papers,
                    "count": 0,
                    "papers": [],
                    "message": f"No papers found for date {date}. The date may not have any updates, or it may be a future date."
                }
            else:
                result = {
                    "date": date,
                    "num_papers_requested": num_papers,
                    "count": len(papers),
                    "papers": papers
                }
            
            return [TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]
        
        elif name == "download_paper_pdf":
            pdf_url = arguments["pdf_url"]
            arxiv_id = arguments.get("arxiv_id")
            
            processor = get_processor()
            
            # Create a minimal paper dict for download
            paper = {
                "pdf_url": pdf_url,
                "arxiv_id": arxiv_id or pdf_url.split("/")[-1].replace(".pdf", "")
            }
            
            pdf_path = processor.download_paper_pdf(paper)
            
            result = {
                "arxiv_id": paper["arxiv_id"],
                "pdf_path": str(pdf_path),
                "exists": pdf_path.exists()
            }
            
            return [TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]
        
        elif name == "extract_pdf_text":
            pdf_path = Path(arguments["pdf_path"])
            
            processor = get_processor()
            text = processor.extract_text(pdf_path)
            
            result = {
                "pdf_path": str(pdf_path),
                "text_length": len(text),
                "text": text
            }
            
            return [TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]
        
        elif name == "convert_pdf_to_markdown":
            pdf_path = Path(arguments["pdf_path"])
            save_to_file = arguments.get("save_to_file", False)
            
            processor = get_processor()
            markdown = processor.convert_to_markdown(pdf_path)
            
            result = {
                "pdf_path": str(pdf_path),
                "markdown_length": len(markdown),
                "markdown": markdown
            }
            
            if save_to_file:
                md_path = processor.convert_and_save_markdown(pdf_path)
                result["markdown_path"] = str(md_path)
            
            return [TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]
        
        elif name == "generate_daily_summary":
            papers = arguments["papers"]
            output_path = Path(arguments["output_path"])
            include_pdf_text = arguments.get("include_pdf_text", True)
            use_markdown = arguments.get("use_markdown", True)  # Default to Markdown conversion
            
            processor = get_processor()
            
            # Generate markdown content
            markdown_lines = [
                "# Daily ArXiv Papers Summary",
                "",
                f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                "",
                "---",
                ""
            ]
            
            for paper in papers:
                rank = paper.get("rank", "?")
                title = paper.get("title", "Unknown Title")
                authors = paper.get("authors", "Unknown Authors")
                abstract = paper.get("abstract", "")
                arxiv_id = paper.get("arxiv_id", "")
                arxiv_version = paper.get("arxiv_version", "")
                abs_url = paper.get("abs_url", "")
                pdf_url = paper.get("pdf_url", "")
                
                markdown_lines.extend([
                    f"## {rank}. {title}",
                    "",
                    f"**Authors:** {authors}",
                    "",
                    f"**ArXiv ID:** {arxiv_id} ({arxiv_version})",
                    "",
                    f"**Abstract:**",
                    abstract,
                    "",
                    f"**Links:**",
                    f"- [Abstract]({abs_url})",
                    f"- [PDF]({pdf_url})",
                    ""
                ])
                
                # Try to extract PDF content if requested
                if include_pdf_text:
                    try:
                        pdf_path = processor.tmp_dir / f"{arxiv_id}.pdf"
                        if pdf_path.exists():
                            if use_markdown:
                                # Convert to Markdown (preferred for AI analysis)
                                try:
                                    md_path = processor.get_markdown_path(pdf_path)
                                    if not md_path.exists():
                                        # Convert and save
                                        md_path = processor.convert_and_save_markdown(pdf_path)
                                    
                                    # Read the Markdown file
                                    with open(md_path, "r", encoding="utf-8") as f:
                                        markdown_content = f.read()
                                    
                                    # Limit content length for summary (first 10000 chars)
                                    content_preview = markdown_content[:10000]
                                    if len(markdown_content) > 10000:
                                        content_preview += "\n\n... (truncated, full content available in Markdown file)"
                                    
                                    markdown_lines.extend([
                                        "**Paper Content (Markdown):**",
                                        "",
                                        "```markdown",
                                        content_preview,
                                        "```",
                                        "",
                                        f"*Full Markdown file: {md_path}*",
                                        ""
                                    ])
                                except Exception as e:
                                    logger.warning(f"Could not convert PDF to Markdown for {arxiv_id}: {e}, falling back to text extraction")
                                    # Fall back to text extraction
                                    text = processor.extract_text(pdf_path)
                                    markdown_lines.extend([
                                        "**Extracted PDF Text:**",
                                        "",
                                        "```",
                                        text[:5000] + ("..." if len(text) > 5000 else ""),
                                        "```",
                                        ""
                                    ])
                            else:
                                # Use plain text extraction
                                text = processor.extract_text(pdf_path)
                                markdown_lines.extend([
                                    "**Extracted PDF Text:**",
                                    "",
                                    "```",
                                    text[:5000] + ("..." if len(text) > 5000 else ""),
                                    "```",
                                    ""
                                ])
                    except Exception as e:
                        logger.warning(f"Could not extract content for {arxiv_id}: {e}")
                        markdown_lines.append(f"*PDF content extraction failed: {e}*\n")
                
                # Add placeholder sections for AI analysis
                markdown_lines.extend([
                    "### Research Motivation",
                    "",
                    "*To be filled by AI analysis*",
                    "",
                    "### Methodology",
                    "",
                    "*To be filled by AI analysis*",
                    "",
                    "### Data Used",
                    "",
                    "*To be filled by AI analysis*",
                    "",
                    "### Conclusions",
                    "",
                    "*To be filled by AI analysis*",
                    "",
                    "---",
                    ""
                ])
            
            # Write to file
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write("\n".join(markdown_lines))
            
            result = {
                "output_path": str(output_path),
                "papers_count": len(papers),
                "file_size": output_path.stat().st_size
            }
            
            return [TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]
        
        else:
            raise ValueError(f"Unknown tool: {name}")
    
    except Exception as e:
        logger.error(f"Error in tool {name}: {e}", exc_info=True)
        return [TextContent(
            type="text",
            text=json.dumps({"error": str(e)}, indent=2)
        )]


async def main():
    """Main entry point for the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
