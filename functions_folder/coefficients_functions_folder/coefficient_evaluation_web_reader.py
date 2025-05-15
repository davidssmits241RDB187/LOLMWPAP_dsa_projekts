import requests
from bs4 import BeautifulSoup
import re
import time
from classes_folder.team_classes_folder.team_service import Team
from classes_folder.player_classes_folder.player_service import Player
from functions_folder.coefficients_functions_folder.evaluate_function import evaluate_coefficients

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://google.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

import requests
from bs4 import BeautifulSoup
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://google.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

def scrape_and_evaluate_matches():
    base_url = "https://gol.gg"
    url1 = f"{base_url}/esports/home/"

    session = requests.Session()
    response1 = session.get(url1, headers=headers)

    if response1.status_code != 200:
        print(f"Failed to retrieve data: {response1.status_code}")
        return

    soup = BeautifulSoup(response1.text, "html.parser")
    body = soup.body

    matches = []

    # Select all <a> inside <td class="footable-visible">
    match_links = body.select('td.footable-visible a[href]')

    for link in match_links:
        href = link['href']
        # Match your pattern exactly
        if re.match(r"^(\.\./)?game/stats/\d+/page-game/?$", href):
            match_text = link.text.strip()

            if href.startswith(".."):
                full_url = base_url + href[2:]
            elif href.startswith("/"):
                full_url = base_url + href
            else:
                full_url = base_url + "/" + href

            matches.append({
                "text": match_text,
                "url": full_url
            })

    for match in matches:
        print(f"{match['text']} -> {match['url']}")

    print(f"\nTotal matches scraped: {len(matches)}")

