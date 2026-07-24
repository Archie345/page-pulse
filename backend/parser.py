import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def audit_page(url: str):
    # Validate URL
    parsed = urlparse(url)

    if parsed.scheme not in ["http", "https"] or not parsed.netloc:
     raise ValueError("Please enter a valid HTTP or HTTPS URL.")

    start = time.time()

    try:
        response = requests.get(
    url,
    timeout=8,
    allow_redirects=True,
    headers={
        "User-Agent": "PagePulse/1.0"
    }
)
    except requests.exceptions.Timeout:
        raise TimeoutError("Request timed out")
    except requests.exceptions.RequestException:
        raise Exception("Unable to fetch URL")

    response_time = round((time.time() - start) * 1000, 2)

    content_type = response.headers.get("Content-Type", "")

    if "text/html" not in content_type:
        raise ValueError("Response is not HTML")

    soup = BeautifulSoup(response.text, "lxml")

    title = soup.title.string.strip() if soup.title and soup.title.string else ""

    meta = soup.find("meta", attrs={"name": "description"})
    meta_description = meta["content"].strip() if meta and meta.get("content") else ""

    h1_count = len(soup.find_all("h1"))

    missing_alt = sum(
        1 for img in soup.find_all("img")
        if not img.get("alt")
    )

    text = soup.get_text(" ", strip=True)
    word_count = len(text.split())

    return {
        "status": response.status_code,
        "response_time_ms": response_time,
        "title": title,
        "meta_description": meta_description,
        "h1_count": h1_count,
        "missing_alt_images": missing_alt,
        "word_count": word_count
    }