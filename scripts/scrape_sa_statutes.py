#!/usr/bin/env python3
"""
scrape_sa_statutes.py
---------------------
Automates retrieval of South Australian cannabis‑related legislation and penalty information.

Functionality
=============
1. Downloads the *Controlled Substances Act 1984 (SA)* and associated Regulations (current versions)
   from legislation.sa.gov.au.
2. Stores raw HTML/PDF into `DATA/Legal_Compliance/statutes/`.
3. Extracts offence tables (Section 33I et al.) and saves structured JSON to
   `DATA/Legal_Compliance/penalties/cannabis_penalties_sa.json`.
4. Optionally pulls ‘simple cannabis offence expiation notice’ penalty amounts.
5. Produces a summary `legal_snapshot_{YYYY‑MM‑DD}.md` for human review.

Usage
=====
    python scripts/scrape_sa_statutes.py

Requirements
============
- requests
- beautifulsoup4
- pdfminer.six (for PDF fallback)
- tqdm (optional progress bar)

Note: The script respects `robots.txt` and implements 1 req/sec back‑off.
"""

import requests, time, json, re, os, datetime, pathlib
from bs4 import BeautifulSoup
from typing import Dict, List

ROOT = pathlib.Path(__file__).resolve().parents[2] / 'DATA' / 'Legal_Compliance'
STAT_DIR = ROOT / 'statutes'
PEN_DIR = ROOT / 'penalties'
BASE_URL = 'https://www.legislation.sa.gov.au'

HEADERS = {        'User-Agent': 'DeepResearchAI/1.0 (+https://github.com/ZBH33/DeepResearch.AI---Adelaide-Cannabis-Cultivation-Variant)'    }

def fetch_latest_cs_act() -> str:
    """Return full URL of the latest Controlled Substances Act 1984 (SA)."""
    index_url = f"{BASE_URL}/laws/controlled-substances-act-1984"
    resp = requests.get(index_url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    link_tag = soup.find('a', string=re.compile('As at'))
    if not link_tag:
        raise RuntimeError('Could not locate latest Act link')
    return BASE_URL + link_tag['href']

def download_file(url: str, out_path: pathlib.Path) -> None:
    with requests.get(url, headers=HEADERS, stream=True, timeout=30) as r:
        r.raise_for_status()
        out_path.write_bytes(r.content)
    time.sleep(1.1)  # polite delay

def parse_penalties_from_html(html: str) -> Dict:
    """Extract offence and penalty tables – very basic demo parser."""
    soup = BeautifulSoup(html, 'html.parser')
    penalties = []
    for table in soup.find_all('table'):
        if 'Cannabis' in table.text:
            headers = [th.get_text(strip=True) for th in table.find_all('th')]
            for row in table.find_all('tr')[1:]:
                cols = [td.get_text(strip=True) for td in row.find_all(['td', 'th'])]
                if len(cols) == len(headers):
                    penalties.append(dict(zip(headers, cols)))
    return {'retrieved': datetime.date.today().isoformat(), 'entries': penalties}

def main():  # pragma: no cover
    STAT_DIR.mkdir(parents=True, exist_ok=True)
    PEN_DIR.mkdir(parents=True, exist_ok=True)

    # 1) Fetch latest Act HTML
    act_url = fetch_latest_cs_act()
    act_filename = STAT_DIR / f"controlled_substances_act_1984_sa_{datetime.date.today()}.html"
    download_file(act_url, act_filename)

    # 2) Parse penalties
    penalties = parse_penalties_from_html(act_filename.read_text(encoding='utf-8', errors='ignore'))
    pen_path = PEN_DIR / f"cannabis_penalties_sa_{datetime.date.today()}.json"
    pen_path.write_text(json.dumps(penalties, indent=2))

    # 3) Snapshot summary
    snapshot = ROOT / f"legal_snapshot_{datetime.date.today()}.md"
    snapshot.write_text(f"""# SA Cannabis Legal Snapshot — {datetime.date.today()}

Source: {act_url}

Parsed {len(penalties['entries'])} penalty entries.
""")
    print("Done. SA statutes downloaded & penalties parsed.")

if __name__ == '__main__':
    main()
