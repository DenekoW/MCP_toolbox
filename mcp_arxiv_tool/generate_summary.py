#!/usr/bin/env python3
"""Script to fetch papers for 2026-01-09 and generate summary using generate_daily_summary logic."""
import json
import logging
import os
import re
from pathlib import Path
from datetime import datetime

from benty_client import BentyFieldsClient
from pdf_processor import PDFProcessor

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config() -> dict:
    """Load configuration from config.json."""
    config_path = Path(__file__).parent / "config.json"
    if not config_path.exists():
        raise FileNotFoundError(f"config.json not found at {config_path}")
    
    with open(config_path, "r") as f:
        config = json.load(f)
    
    return config

def fill_ai_sections(title, abstract, authors):
    """Fill AI analysis sections based on paper title and abstract."""
    if not OPENAI_AVAILABLE:
        # Fallback: simple extraction from abstract
        return {
            "motivation": "*AI analysis unavailable - install openai package and set OPENAI_API_KEY*",
            "methodology": "*AI analysis unavailable - install openai package and set OPENAI_API_KEY*",
            "data_used": "*AI analysis unavailable - install openai package and set OPENAI_API_KEY*",
            "conclusions": "*AI analysis unavailable - install openai package and set OPENAI_API_KEY*"
        }
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return {
            "motivation": "*AI analysis unavailable - set OPENAI_API_KEY environment variable*",
            "methodology": "*AI analysis unavailable - set OPENAI_API_KEY environment variable*",
            "data_used": "*AI analysis unavailable - set OPENAI_API_KEY environment variable*",
            "conclusions": "*AI analysis unavailable - set OPENAI_API_KEY environment variable*"
        }
    
    try:
        client = openai.OpenAI(api_key=api_key)
        
        prompt = f"""Based on the following research paper information, provide a brief analysis in Chinese:

Title: {title}
Authors: {authors}
Abstract: {abstract}

Please provide a concise analysis in Chinese for each of the following sections:
1. Research Motivation (研究动机): What problem does this research address?
2. Methodology (研究方法): What approach or method does the paper use?
3. Data Used (使用的数据): What data, datasets, or observations are used?
4. Conclusions (结论): What are the main findings or conclusions?

Format your response as JSON with keys: "motivation", "methodology", "data_used", "conclusions". Each value should be a brief paragraph in Chinese (2-3 sentences)."""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a research paper analyst. Provide concise, accurate analysis in Chinese."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1000
        )
        
        content = response.choices[0].message.content.strip()
        
        # Try to parse JSON response
        try:
            # Extract JSON from response (in case it's wrapped in markdown code blocks)
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                content = json_match.group(0)
            result = json.loads(content)
            return result
        except json.JSONDecodeError:
            # If not JSON, try to extract sections manually
            logger.warning("Failed to parse AI response as JSON, using fallback")
            return {
                "motivation": content[:200] + "..." if len(content) > 200 else content,
                "methodology": "*Could not parse AI response*",
                "data_used": "*Could not parse AI response*",
                "conclusions": "*Could not parse AI response*"
            }
    except Exception as e:
        logger.warning(f"AI analysis failed: {e}")
        return {
            "motivation": f"*AI analysis failed: {str(e)}*",
            "methodology": f"*AI analysis failed: {str(e)}*",
            "data_used": f"*AI analysis failed: {str(e)}*",
            "conclusions": f"*AI analysis failed: {str(e)}*"
        }

def generate_daily_summary(papers, output_path, processor, include_pdf_text=False, use_markdown=True):
    """Generate markdown summary from papers (same logic as MCP tool)."""
    output_path = Path(output_path)
    
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
                    # Download PDF if it doesn't exist
                    try:
                        logger.info(f"Downloading PDF for {arxiv_id}...")
                        pdf_path = processor.download_paper_pdf(paper)
                        if pdf_path.exists():
                            if use_markdown:
                                try:
                                    md_path = processor.convert_and_save_markdown(pdf_path)
                                    with open(md_path, "r", encoding="utf-8") as f:
                                        markdown_content = f.read()
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
                        logger.warning(f"Could not download/extract content for {arxiv_id}: {e}")
                        markdown_lines.append(f"*PDF content extraction failed: {e}*\n")
            except Exception as e:
                logger.warning(f"Could not extract content for {arxiv_id}: {e}")
                markdown_lines.append(f"*PDF content extraction failed: {e}*\n")
        
        # Add AI-filled sections
        ai_sections = fill_ai_sections(title, abstract, authors)
        markdown_lines.extend([
            "### Research Motivation",
            "",
            ai_sections.get("motivation", "*AI analysis unavailable*"),
            "",
            "### Methodology",
            "",
            ai_sections.get("methodology", "*AI analysis unavailable*"),
            "",
            "### Data Used",
            "",
            ai_sections.get("data_used", "*AI analysis unavailable*"),
            "",
            "### Conclusions",
            "",
            ai_sections.get("conclusions", "*AI analysis unavailable*"),
            "",
            "---",
            ""
        ])
    
    # Write to file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(markdown_lines))
    
    return {
        "output_path": str(output_path),
        "papers_count": len(papers),
        "file_size": output_path.stat().st_size
    }

def main():
    """Main function to fetch papers and generate summary."""
    # Load config
    config = load_config()
    benty_config = config.get("benty_fields", {})
    email = benty_config.get("email", "")
    password = benty_config.get("password", "")
    
    if not email or not password:
        raise ValueError("benty_fields.email and benty_fields.password must be set in config.json")
    
    # Get date (2026-01-09)
    date = "2026-01-09"
    num_papers = config.get("num_papers", 10)
    output_dir = config.get("output_dir", "./summaries")
    
    # Initialize client and processor
    logger.info("Logging in to benty-fields.com...")
    client = BentyFieldsClient(email, password)
    client.login()
    
    # Initialize processor
    tmp_dir = config.get("tmp_dir")
    if tmp_dir:
        tmp_dir = Path(tmp_dir)
    processor = PDFProcessor(tmp_dir=tmp_dir)
    
    # Fetch papers
    logger.info(f"Fetching papers for {date}...")
    papers = client.fetch_daily_papers(date, num_papers=num_papers)
    
    if len(papers) == 0:
        logger.warning(f"No papers found for date {date}")
        return
    
    logger.info(f"Found {len(papers)} papers")
    
    # Skip PDF download since we don't need PDF content
    # logger.info("Downloading PDFs...")
    # for paper in papers:
    #     try:
    #         processor.download_paper_pdf(paper)
    #     except Exception as e:
    #         logger.warning(f"Failed to download PDF for {paper.get('arxiv_id', 'unknown')}: {e}")
    
    # Generate summary (without PDF content, with AI analysis)
    output_path = Path(output_dir) / f"summary_{date.replace('-', '')}.md"
    logger.info(f"Generating summary at {output_path}...")
    logger.info("Filling AI analysis sections...")
    result = generate_daily_summary(papers, output_path, processor, include_pdf_text=False, use_markdown=True)
    
    logger.info(f"Summary generated successfully!")
    logger.info(f"Output: {result['output_path']}")
    logger.info(f"Papers: {result['papers_count']}")
    logger.info(f"File size: {result['file_size']} bytes")

if __name__ == "__main__":
    main()
