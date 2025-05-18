from bs4 import BeautifulSoup
import requests


headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"}
def read_links():
    url1 = "https://gol.gg/esports/home/"
    response1 = requests.get(url1,headers=headers)
    soup1 = BeautifulSoup(response1.text,"html.parser") 
    table = soup1.select_one("#lastgames_tab > table")
    cells = table.select("tr > td > a")
    links = []
    for cell in cells:
        links.append(cell.get_text(strip=True),"-",cell["href"])
    print(links)
read_links()