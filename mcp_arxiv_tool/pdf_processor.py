"""PDF download and text extraction utilities."""
import requests
from pathlib import Path
import tempfile
from typing import Optional
import logging

try:
    import fitz  # PyMuPDF
    PYMUPDF_AVAILABLE = True
except ImportError:
    PYMUPDF_AVAILABLE = False

try:
    import pdfplumber
    PDFPLUMBER_AVAILABLE = True
except ImportError:
    PDFPLUMBER_AVAILABLE = False

try:
    import pymupdf4llm
    PYMUPDF4LLM_AVAILABLE = True
except ImportError:
    PYMUPDF4LLM_AVAILABLE = False

logger = logging.getLogger(__name__)


class PDFProcessor:
    """Handles PDF download and text extraction."""
    
    def __init__(self, tmp_dir: Optional[Path] = None):
        """
        Initialize PDF processor.
        
        Args:
            tmp_dir: Directory to store downloaded PDFs. If None, uses system temp.
        """
        if tmp_dir is None:
            tmp_dir = Path(tempfile.gettempdir()) / "benty_arxiv_pdfs"
        
        self.tmp_dir = Path(tmp_dir)
        self.tmp_dir.mkdir(parents=True, exist_ok=True)
        
        # Check for PDF libraries (at least one is needed)
        if not PYMUPDF_AVAILABLE and not PDFPLUMBER_AVAILABLE:
            raise RuntimeError(
                "No PDF library available. Please install PyMuPDF (pip install pymupdf) "
                "or pdfplumber (pip install pdfplumber)"
            )
    
    def download_pdf(self, pdf_url: str, save_path: Optional[Path] = None) -> Path:
        """
        Download a PDF from a URL.
        
        Args:
            pdf_url: URL of the PDF to download
            save_path: Path to save the PDF. If None, uses arxiv_id from URL.
        
        Returns:
            Path to the downloaded PDF file.
        """
        if save_path is None:
            # Try to extract arxiv_id from URL
            filename = pdf_url.split("/")[-1]
            if not filename.endswith(".pdf"):
                filename = f"{filename}.pdf"
            save_path = self.tmp_dir / filename
        
        save_path = Path(save_path)
        
        # Skip if already exists
        if save_path.exists():
            logger.info(f"PDF already exists: {save_path}")
            return save_path
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        logger.info(f"Downloading PDF from {pdf_url}")
        with requests.get(pdf_url, headers=headers, stream=True, timeout=30) as r:
            r.raise_for_status()
            with open(save_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        
        logger.info(f"Downloaded PDF to {save_path}")
        return save_path
    
    def download_paper_pdf(self, paper: dict) -> Path:
        """
        Download PDF for a paper dictionary.
        
        Args:
            paper: Paper dictionary with 'arxiv_id' and 'pdf_url' keys.
        
        Returns:
            Path to the downloaded PDF.
        """
        arxiv_id = paper["arxiv_id"]
        pdf_url = paper["pdf_url"]
        
        pdf_path = self.tmp_dir / f"{arxiv_id}.pdf"
        
        if pdf_path.exists():
            return pdf_path
        
        return self.download_pdf(pdf_url, pdf_path)
    
    def extract_text(self, pdf_path: Path) -> str:
        """
        Extract text from a PDF file.
        
        Args:
            pdf_path: Path to the PDF file.
        
        Returns:
            Extracted text as a string.
        """
        pdf_path = Path(pdf_path)
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        text = ""
        
        # Try PyMuPDF first (faster)
        if PYMUPDF_AVAILABLE:
            try:
                doc = fitz.open(str(pdf_path))
                for page in doc:
                    text += page.get_text()
                doc.close()
                logger.info(f"Extracted text using PyMuPDF from {pdf_path}")
                return text
            except Exception as e:
                logger.warning(f"PyMuPDF extraction failed: {e}, trying pdfplumber")
        
        # Fall back to pdfplumber
        if PDFPLUMBER_AVAILABLE:
            try:
                with pdfplumber.open(str(pdf_path)) as pdf:
                    for page in pdf.pages:
                        page_text = page.extract_text()
                        if page_text:
                            text += page_text + "\n"
                logger.info(f"Extracted text using pdfplumber from {pdf_path}")
                return text
            except Exception as e:
                logger.error(f"pdfplumber extraction failed: {e}")
                raise
        
        raise RuntimeError("No PDF extraction library available")
    
    def convert_to_markdown(self, pdf_path: Path) -> str:
        """
        Convert PDF to Markdown format using pymupdf4llm.
        
        Args:
            pdf_path: Path to the PDF file.
        
        Returns:
            Markdown content as a string.
        """
        pdf_path = Path(pdf_path)
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        if not PYMUPDF4LLM_AVAILABLE:
            raise RuntimeError(
                "pymupdf4llm is not available. Please install it: pip install pymupdf4llm"
            )
        
        try:
            logger.info(f"Converting PDF to Markdown: {pdf_path}")
            markdown = pymupdf4llm.to_markdown(pdf_path, show_progress=False)
            logger.info(f"Successfully converted PDF to Markdown: {pdf_path}")
            return markdown
        except Exception as e:
            logger.error(f"Failed to convert PDF to Markdown: {e}")
            raise RuntimeError(f"PDF to Markdown conversion failed: {e}")
    
    def get_markdown_path(self, pdf_path: Path) -> Path:
        """
        Get the path for the Markdown file corresponding to a PDF.
        
        Args:
            pdf_path: Path to the PDF file.
        
        Returns:
            Path to the corresponding Markdown file.
        """
        pdf_path = Path(pdf_path)
        return pdf_path.with_suffix(".md")
    
    def convert_and_save_markdown(self, pdf_path: Path, markdown_path: Optional[Path] = None) -> Path:
        """
        Convert PDF to Markdown and save to file.
        
        Args:
            pdf_path: Path to the PDF file.
            markdown_path: Path to save Markdown. If None, uses same path with .md extension.
        
        Returns:
            Path to the saved Markdown file.
        """
        pdf_path = Path(pdf_path)
        if markdown_path is None:
            markdown_path = self.get_markdown_path(pdf_path)
        else:
            markdown_path = Path(markdown_path)
        
        # Check if Markdown already exists
        if markdown_path.exists():
            logger.info(f"Markdown already exists: {markdown_path}")
            return markdown_path
        
        # Convert and save
        markdown = self.convert_to_markdown(pdf_path)
        
        markdown_path.parent.mkdir(parents=True, exist_ok=True)
        with open(markdown_path, "w", encoding="utf-8") as f:
            f.write(markdown)
        
        logger.info(f"Saved Markdown to: {markdown_path}")
        return markdown_path
