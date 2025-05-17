from services.team_service import Team
from services.player_service import Player
from data.data_types import RowData, PlayerData

import dataclasses
import os.path
import json
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"}
season = "season-S15/split-Spring/tournament-ALL/"
teams_list_address = "https://gol.gg/teams/list/"
teams_stats_address = "https://gol.gg/teams/"

lolesports_address = "https://lolesports.com/en-GB/"

class Serialization:
    def encode_value(x):
        #print(f"Encoding value: {x}")
        if dataclasses.is_dataclass(x):
            return dataclasses.asdict(x)
        return x
    def get_float(x):
        x = x.replace("%", "")
        x = float(x) / 100
        return x

class DataService:
    def __init__(self):
        self.teams = {}
        try:
            if os.path.isfile("data/data.json"):
                with open("data/data.json", "r") as file:
                    self.teams = json.load(file)
                    for team in self.teams:
                        team_object = Team()
                        for key in self.teams[team].keys():
                            setattr(team_object, key, self.teams[team][key])
                        self.teams[team] = team_object
                print(f"Loaded {len(self.teams)} teams from file.")
            else:
                self.fetch_teams()
        except Exception as e:
            print("Error loading data")
            print(e.args[0])
            self.fetch_teams()

    def fetch_data(url):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            if response.status_code != 200:
                raise Exception({response.status_code})
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup
        except requests.exceptions.RequestException as e:
            print("Request Exception")
                
        except requests.exceptions.HTTPError as e:
            print("HTTP Error")
            print(e.args[0])

    def fetch_teams(self):
        print("Fetching teams...")
        page = DataService.fetch_data(teams_list_address + season)
        table = page.find("table", class_="playerslist")
        links = table.find_all('a')
        print(f"Found {len(links)} links.")
        for link in links:
            team_stats_address = teams_stats_address + link['href'][2:] # remove ./ from link
            team_name = link.string
            team_stats =  DataService.fetch_data(team_stats_address)
            team_rows = team_stats.find_all("tr")
            team = Team()
            team.name = team
            last_row = ""
            for row in team_rows:
                row_data = row.find_all("td")
                
                if len(row_data) < 2:
                    continue
                
                if row_data[0].text in RowData:
                    last_row = row_data[0].text
                    if len(row_data) > 1:
                        stat_percent = row_data[1].select("div.col-auto.pl-1.position-absolute")
                        if stat_percent:
                            stat_value = Serialization.get_float(stat_percent[0].text)
                        else:
                            stat_value = row_data[1].text
                            stat_value = stat_value.replace("+", "")
                    setattr(team, RowData[row_data[0].text], stat_value)
                    continue
                
                if last_row == "Win Rate : ":
                    last_row = row_data[0].text
                    stat_percent = row_data[1].select("div.col-auto.pl-1.position-absolute")
                    if stat_percent:
                        stat_value = Serialization.get_float(stat_percent[0].text)
                    setattr(team, RowData["%WinRate"], stat_value)
                    continue

                if row_data[0].text in PlayerData:
                    player = Player()
                    player.team = team_name
                    player.role = PlayerData[row_data[0].text]
                    player.name = row_data[1].select("a")[0].text
                    player.kda = row_data[2].text
                    player.kp = Serialization.get_float(row_data[3].text)
                    player.vspm = row_data[4].text
                    player.dmg = Serialization.get_float(row_data[5].select("span")[0].text)
                    player.gold = Serialization.get_float(row_data[6].select("span")[0].text)
                    champions = row_data[7].find_all("span", class_="text-center")
                    matches_played = 0
                    for champion in champions:
                        champion_name = champion.select("img")[0].get("alt")
                        champion_text = champion.text
                        champion_played_list = champion_text.split("\n")
                        champion_played = champion_played_list[-1].strip()
                        player.add_champion(champion_name, champion_played)
                    player.matches_played = matches_played
                    team.add_player(player.role, player)
            self.teams[team_name] = team
            print(f"Fetched team: {team_name}")
        try:
            with open("data/data.json", "w") as file:
                json.dump(self.teams, file, default=Serialization.encode_value)
        except Exception as e:
            print("Error saving data")
            print(e.args[0])

    def get_team(self, team_name):
        print("Getting team...")
        try:
            if team_name in self.teams:
                print(f"Found team {team_name}")
                return self.teams[team_name]
            else:
                print(f"Team {team_name} not found.")
        except Exception as e:
            print("Error getting team")
            print(e.args[0])
