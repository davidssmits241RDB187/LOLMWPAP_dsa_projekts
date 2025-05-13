from team_service import Team
from team_data_types import TeamRow
from dataclasses import dataclass
import os.path
import json
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"}
gol_address = "https://gol.gg/teams/list/season-S15/split-Spring/tournament-ALL/"
lolesports_address = "https://lolesports.com/en-GB/"

class Serialization:
    def encode_value(x):
    if dataclasses.is_dataclass(x):
        return dataclasses.asdict(x)
    elif isinstance(x, datetime.datetime):
        return x.isoformat()
    # other special cases... 

    return x

class DataService:
    def __init__(self):
        self.teams = {}
        if os.path.isfile("data.json"):
            with open("data.json", "r") as file:
                self.teams = json.load(file)
        else:
            self.fetch_teams()

    def fetch_teams(self):
        print("Fetching teams...")
        try:
            response = requests.get(gol_address, headers=headers)
            response.raise_for_status()
            print(response.status_code)
            if response.status_code != 200:
                raise Exception({response.status_code})
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find("table", class_="playerslist")
            links = table.find_all('a')
            print(f"Found {len(links)} links.")
            for link in links:
                link_value = link.string
                table_row = link.parent.parent
                team_stats = table_row.find_all('td', class_="text-center")
                team = Team()
                team.team_name = link_value
                for i in range(0, len(team_stats)):
                    print(team_stats[i].string)
                    stat_value = team_stats[i].string
                    setattr(team, TeamRow[i], stat_value)
                self.teams[link_value] = team
            with open("data.json", "w") as file:
                json.dump(self.teams, file, default=lambda o: if hasattr(o, '__json__')
        except requests.exceptions.RequestException as e:
            print("Request Exception")
                
        except requests.exceptions.HTTPError as e:
            print("HTTP Error")
            print(e.args[0])

    def get_team(self, team_name):
        print("Getting team...")
        try:
            if team_name in self.teams:
                return self.teams[team_name]
            else:
                print(f"Team {team_name} not found.")
        except Exception as e:
            print("Error getting team")
            print(e.args[0])
