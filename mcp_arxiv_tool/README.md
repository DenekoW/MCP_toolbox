# Benty Fields ArXiv MCP Server

An MCP (Model Context Protocol) server that fetches daily top N arXiv papers from [benty-fields.com](https://www.benty-fields.com), downloads PDFs, extracts text, and generates summary documents for AI analysis.

## Features

- 🔐 Automatic login to benty-fields.com
- 📄 Fetches top N daily papers ranked by your reading preferences (configurable, default: 10)
- 📥 Downloads PDFs to temporary storage
- 📝 Extracts text from PDFs for AI analysis
- 📊 Generates structured markdown summaries with placeholders for AI analysis

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure credentials in `config.json`:
```json
{
  "benty_fields": {
    "email": "your-email@example.com",
    "password": "your-password"
  },
  "tmp_dir": null,
  "output_dir": "./summaries"
}
```

- `benty_fields.email`: Your benty-fields.com email
- `benty_fields.password`: Your benty-fields.com password
- `date`: Date in YYYY-MM-DD format, or `null` to use today's date (default: `null`)
- `num_papers`: Number of top papers to fetch (default: 10)
- `tmp_dir`: Optional custom path for PDF storage (default: system temp directory)
- `output_dir`: Directory for generated summary documents

## MCP Server Setup

### For Cursor IDE

Add to your Cursor MCP configuration (usually in `~/.cursor/mcp.json` or similar):

```json
{
  "mcpServers": {
    "benty-fields-arxiv": {
      "command": "python",
      "args": ["/path/to/mcp_arxiv_tool/server.py"]
    }
  }
}
```

Make sure to use the absolute path to `server.py`.

## Available Tools

### 1. `fetch_daily_papers`

Fetches top N papers for a given date from benty-fields.com.

**Parameters:**
- `date` (optional): Date in YYYY-MM-DD format. If not provided, uses value from config.json. If config.json has `null`, uses today's date.
- `num_papers` (optional): Number of top papers to fetch. Defaults to value in config.json (default: 10).

**Returns:**
- If papers are found: Object with:
  - `date`: The date queried
  - `num_papers_requested`: Number of papers requested
  - `count`: Number of papers found
  - `papers`: List of paper dictionaries with:
    - `rank`: Paper rank (1-N)
    - `title`: Paper title
    - `authors`: Author list
    - `abstract`: Paper abstract
    - `arxiv_id`: ArXiv ID (e.g., "2601.04344")
    - `arxiv_version`: Full version string (e.g., "2601.04344v1")
    - `pdf_url`: URL to PDF
    - `abs_url`: URL to abstract page
- If no papers are found: Object with:
  - `date`: The date queried
  - `num_papers_requested`: Number of papers requested
  - `count`: 0
  - `papers`: Empty array
  - `message`: Message indicating no papers were found for that date

### 2. `download_paper_pdf`

Downloads a PDF for a specific paper.

**Parameters:**
- `pdf_url` (required): URL of the PDF to download
- `arxiv_id` (optional): ArXiv ID for filename

**Returns:**
- Path to downloaded PDF file

### 3. `extract_pdf_text`

Extracts plain text from a downloaded PDF file.

**Parameters:**
- `pdf_path` (required): Path to the PDF file

**Returns:**
- Extracted text content

### 4. `convert_pdf_to_markdown`

Converts a PDF file to Markdown format. This is preferred for AI analysis as it preserves document structure, formatting, and is easier for AI models to process.

**Parameters:**
- `pdf_path` (required): Path to the PDF file
- `save_to_file` (optional): Whether to save Markdown to a file (default: false). If true, saves to same location as PDF with .md extension.

**Returns:**
- Markdown content and optionally the path to saved Markdown file

### 5. `generate_daily_summary`

Generates a markdown summary document from processed papers. By default, converts PDFs to Markdown format for better AI analysis.

**Parameters:**
- `papers` (required): Array of paper dictionaries
- `output_path` (required): Path where the summary should be saved
- `include_pdf_text` (optional): Whether to include PDF content in the summary (default: true)
- `use_markdown` (optional): Whether to convert PDF to Markdown format (default: true). If false, uses plain text extraction.

**Returns:**
- Summary of the generated document

## Usage Example

1. **Fetch today's papers:**
```
Use tool: fetch_daily_papers
```

2. **Download PDFs (optional, can be done automatically):**
```
Use tool: download_paper_pdf with pdf_url from paper data
```

3. **Convert PDFs to Markdown (optional, recommended for AI analysis):**
```
Use tool: convert_pdf_to_markdown with pdf_path and save_to_file=true
```

4. **Generate summary document:**
```
Use tool: generate_daily_summary with papers array and output_path
```

5. **Analyze with Cursor AI:**
   - Open the generated markdown file
   - Ask Cursor AI to fill in the "Research Motivation", "Methodology", "Data Used", and "Conclusions" sections for each paper

## Workflow

The typical workflow is:

1. Fetch daily papers using `fetch_daily_papers`
2. Optionally download PDFs (they're cached, so re-downloads are skipped)
3. Generate summary document with `generate_daily_summary`
4. Use Cursor AI to analyze the PDF content (converted to Markdown) and fill in the analysis sections

## Dependencies

- `mcp`: MCP Python SDK
- `requests`: HTTP requests
- `beautifulsoup4`: HTML parsing
- `pymupdf`: PDF text extraction (primary)
- `pdfplumber`: PDF text extraction (fallback)
- `pymupdf4llm`: PDF to Markdown conversion (recommended for AI analysis)

At least one PDF library (pymupdf or pdfplumber) is required.

## Notes

- PDFs are cached in the temporary directory to avoid re-downloading
- The server maintains a session with benty-fields.com after login
- PDF text extraction uses PyMuPDF by default, falls back to pdfplumber if needed
- PDF to Markdown conversion uses `pymupdf4llm` for better structure preservation and AI analysis
- Generated summaries include PDF content (as Markdown by default) and placeholders for AI analysis that Cursor can fill in

## Troubleshooting

**Login fails:**
- Check your credentials in `config.json`
- Ensure your benty-fields.com account is active

**PDF download fails:**
- Check your internet connection
- Some PDFs may be temporarily unavailable

**PDF text extraction/conversion fails:**
- Ensure at least one PDF library is installed (pymupdf or pdfplumber)
- For Markdown conversion, ensure `pymupdf4llm` is installed: `pip install pymupdf4llm`
- Some PDFs may be image-based and require OCR (not currently supported)

## License

MIT
