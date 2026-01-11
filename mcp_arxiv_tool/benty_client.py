"""Benty Fields client for fetching daily arXiv papers."""
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
from datetime import datetime


class BentyFieldsClient:
    """Client for interacting with benty-fields.com."""
    
    def __init__(self, email: str, password: str):
        """Initialize client with credentials."""
        self.email = email
        self.password = password
        self.session = requests.Session()
        self._logged_in = False
    
    def login(self) -> bool:
        """Login to benty-fields.com and maintain session."""
        login_url = "https://www.benty-fields.com/login"
        
        # Get login page to extract CSRF token
        resp = self.session.get(login_url)
        resp.raise_for_status()
        
        soup = BeautifulSoup(resp.text, "html.parser")
        csrf_token_input = soup.find("input", {"name": "csrf_token"})
        
        if not csrf_token_input:
            raise RuntimeError("Could not find CSRF token on login page")
        
        csrf_token = csrf_token_input["value"]
        
        # Perform login
        payload = {
            "email": self.email,
            "password": self.password,
            "csrf_token": csrf_token
        }
        
        resp = self.session.post(login_url, data=payload)
        resp.raise_for_status()
        
        # Check if login was successful
        if "Logout" not in resp.text:
            raise RuntimeError("Login failed - check credentials")
        
        self._logged_in = True
        return True
    
    def _ensure_logged_in(self):
        """Ensure we're logged in before making requests."""
        if not self._logged_in:
            self.login()
    
    def fetch_daily_papers(self, date: Optional[str] = None, num_papers: int = 10) -> List[Dict]:
        """
        Fetch top N papers for a given date.
        
        Args:
            date: Date in YYYY-MM-DD format. If None, uses today's date.
            num_papers: Number of top papers to fetch. Default is 10.
        
        Returns:
            List of paper dictionaries with rank, title, authors, abstract, etc.
        """
        self._ensure_logged_in()
        
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        url = f"https://www.benty-fields.com/daily_arXiv_results?date={date}"
        resp = self.session.get(url)
        resp.raise_for_status()
        
        soup = BeautifulSoup(resp.text, "html.parser")
        paper_divs = soup.find_all("div", class_="paper")[:num_papers]
        
        papers = []
        for paper_div in paper_divs:
            try:
                paper_info = self._parse_paper(paper_div)
                papers.append(paper_info)
            except Exception as e:
                # Log error but continue with other papers
                print(f"Error parsing paper: {e}")
                continue
        
        return papers
    
    def _parse_paper(self, paper_div) -> Dict:
        """Parse a paper div element into a dictionary."""
        h4 = paper_div.find("h4", class_="paper_row")
        if not h4:
            raise ValueError("Could not find paper title")
        
        raw_title = h4.get_text(strip=True)
        rank_str, title = raw_title.split(".", 1)
        
        authors_p = paper_div.find("p", class_="paper_row")
        if not authors_p:
            raise ValueError("Could not find authors")
        authors = authors_p.get_text(strip=True)
        
        abs_link = paper_div.find("a", href=lambda x: x and "arxiv.org/abs" in x)
        if not abs_link:
            raise ValueError("Could not find arXiv abstract link")
        
        pdf_link = paper_div.find("a", href=lambda x: x and x.endswith(".pdf"))
        if not pdf_link:
            raise ValueError("Could not find PDF link")
        
        arxiv_version = abs_link.get_text(strip=True)
        arxiv_id = arxiv_version.split("v")[0]
        
        abstract_p = paper_div.find("p", attrs={"name": "abstract_field"})
        abstract = abstract_p.get_text(strip=True) if abstract_p else ""
        
        return {
            "rank": int(rank_str),
            "title": title.strip(),
            "authors": authors,
            "abstract": abstract,
            "arxiv_id": arxiv_id,
            "arxiv_version": arxiv_version,
            "pdf_url": pdf_link["href"],
            "abs_url": abs_link["href"],
        }
