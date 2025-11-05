# scrape_aristocrat_ir_recursive_with_pdfs.py
import os, requests, csv, time, re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

BASE = "https://ir.aristocrat.com/"
DOMAIN = urlparse(BASE).netloc
HEADERS = {"User-Agent": "Aristocrat-IR-Scraper/3.0 (+contact@example.com)"}

visited = set()
results = []
PDF_DIR = "pdfs"

# Create folder for PDFs
os.makedirs(PDF_DIR, exist_ok=True)

def crawl(url, depth=0, max_depth=3):
    """Recursively crawl internal pages and download PDFs."""
    if url in visited or depth > max_depth:
        return
    visited.add(url)

    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code != 200 or "text/html" not in r.headers.get("Content-Type", ""):
            return
    except Exception:
        return

    soup = BeautifulSoup(r.text, "html.parser")

    # --- Find PDFs ---
    for a in soup.select('a[href$=".pdf"]'):
        pdf_url = urljoin(url, a["href"])
        title = a.get_text(strip=True) or os.path.basename(pdf_url)
        results.append({"type": "pdf", "url": pdf_url, "title": title})

        # Download the PDF
        try:
            pdf_name = os.path.basename(urlparse(pdf_url).path)
            pdf_path = os.path.join(PDF_DIR, pdf_name)
            if not os.path.exists(pdf_path):  # skip if already downloaded
                print("Downloading:", pdf_name)
                pdf_data = requests.get(pdf_url, headers=HEADERS, timeout=30)
                if pdf_data.status_code == 200:
                    with open(pdf_path, "wb") as f:
                        f.write(pdf_data.content)
        except Exception as e:
            print("Failed to download:", pdf_url, "->", e)

    # --- Find YouTube / Brightcove embeds ---
    for iframe in soup.find_all("iframe"):
        src = iframe.get("src", "")
        if "youtube.com" in src or "youtu.be" in src:
            results.append({"type": "youtube", "url": src, "title": "YouTube video"})
        elif "brightcove" in src or ".mp4" in src:
            results.append({"type": "video", "url": src, "title": "Brightcove/MP4"})

    # --- Follow internal links ---
    for a in soup.find_all("a", href=True):
        link = urljoin(url, a["href"])
        parsed = urlparse(link)
        if DOMAIN in parsed.netloc and link not in visited:
            if any(link.lower().endswith(ext) for ext in [".pdf", ".jpg", ".png", ".zip"]):
                continue
            crawl(link, depth + 1, max_depth)

    time.sleep(1)  # be polite

# --- Run the crawl ---
crawl(BASE, depth=0, max_depth=3)

# --- Save all found links to CSV ---
with open("aristocrat_ir_sources_recursive_with_pdfs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["type", "url", "title"])
    writer.writeheader()
    writer.writerows(results)

print(f"\nDone! Found {len(results)} items.")
print(f"All PDFs saved to ./{PDF_DIR}/")
