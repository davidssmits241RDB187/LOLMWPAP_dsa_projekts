from services.team_service import Team
from services.player_service import Player
from services.coefficient_service import Coefficients
from data.data_types import RowData, PlayerData, MatchData, CoefficientRoles, CoefficientPlayerAttributes

import dataclasses
import os.path
import json
import requests
import unicodedata
import ast
from datetime import datetime, timedelta
from bs4 import BeautifulSoup, Tag

headers = {"Cookie": "PHPSESSID=lefonepn6793q6ij1ve09e9idh", "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"}
season = "season-S15/split-Spring/tournament-ALL/"
teams_list_address = "https://gol.gg/teams/list/"
teams_stats_address = "https://gol.gg/teams/"
tournament_list_address = "https://gol.gg/tournament/ajax.trlist.php"
tournament_address = "https://gol.gg/tournament/tournament-matchlist/"
golgg_address = "https://gol.gg/"

leaguepedia_address = "https://lol.fandom.com/wiki/League_of_Legends_Esports_Wiki"

class Serialization:
    @staticmethod
    def encode_value(x):
        if dataclasses.is_dataclass(x) and not isinstance(x, type):
            return dataclasses.asdict(x)
        return x
    
    @staticmethod
    def get_float(x):
        x = x.replace("%", "")
        x = float(x) / 100
        return x

    @staticmethod
    def parse_str(s):
        try:
            return ast.literal_eval(str(s))
        except:
            return s

class DataService:
    def __init__(self):
        self.teams = {}
        self.coefficients = Coefficients()

        try:
            if os.path.isfile("data/team_data.json"):
                with open("data/team_data.json", "r") as file:
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
            print("Error loading teams")
            print(e.args[0])
            self.fetch_teams()
        
        try:
            if os.path.isfile("data/coefficient_data.json"):
                with open("data/coefficient_data.json", "r") as file:
                    file_data = json.load(file)
                    for key in file_data:
                        setattr(self.coefficients, key, file_data[key])
                print(f"Loaded coefficients from file.")
            else:
                self.fetch_coefficients()
        except Exception as e:
            print("Error loading coefficients")
            print(e.args[0])
            self.fetch_coefficients()

    @staticmethod
    def fetch_data(url):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            if response.status_code != 200:
                raise Exception({response.status_code})
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup
        except requests.exceptions.RequestException as e:
            print("HTTP Error")
            print(e.args[0])
        
    @staticmethod
    def fetch_data_api(url, request):
        try:
            response = requests.post(url, data=request, headers=headers)
            response.raise_for_status()
            if response.status_code != 200:
                raise Exception({response.status_code})
            return response
        except requests.exceptions.RequestException as e:
            print("HTTP Error")
            print(e.args[0])

    def fetch_teams(self):
        print("Fetching teams...")
        data = DataService.fetch_data(teams_list_address + season)
        if data is None: return
        
        table = data.find("table", class_="table_list")
        if not isinstance(table, Tag): return
        
        links = table.find_all('a')
        print(f"Found {len(links)} links.")
        for link in links:
            if not isinstance(link, Tag): continue
            team_stats_address = teams_stats_address + str(link["href"][2:]) # remove ./ from link
            team_stats =  DataService.fetch_data(team_stats_address)
            if team_stats is None: continue

            team_rows = team_stats.find_all("tr")
            team = Team()
            team_name = link.string
            if team_name is not None: team.name = team_name
            
            last_row = ""
            for row in team_rows:
                if not isinstance(row, Tag): continue
                row_data = row.find_all("td")
                
                if len(row_data) < 2:
                    continue
                
                
                if row_data[0].text in RowData:
                    last_row = row_data[0].text
                    if len(row_data) > 1:
                        row_data1 = row_data[1]
                        if not isinstance(row_data1, Tag): continue

                        stat_percent = row_data1.select("div.col-auto.pl-1.position-absolute")
                        if stat_percent:
                            stat_value = Serialization.get_float(stat_percent[0].text)
                        else:
                            stat_value = row_data[1].text
                            stat_value = stat_value.replace("+", "")
                            offset = stat_value.find(" (")
                            if offset != -1:
                                stat_value = stat_value[:offset]
                            stat_value = Serialization.parse_str(stat_value)
                    setattr(team, RowData[row_data[0].text], stat_value)
                    continue
                
                if last_row == "Win Rate : ":
                    last_row = row_data[0].text
                    row_data1 = row_data[1]
                    if not isinstance(row_data1, Tag): continue
                    
                    stat_percent = row_data1.select("div.col-auto.pl-1.position-absolute")
                    if stat_percent:
                        stat_value = Serialization.get_float(stat_percent[0].text)
                    setattr(team, RowData["%WinRate"], stat_value)
                    continue

                if row_data[0].text in PlayerData:
                    row_data1 = row_data[1]
                    row_data5 = row_data[5]
                    row_data6 = row_data[6]
                    row_data7 = row_data[7]
                    if not isinstance(row_data1, Tag): continue
                    if not isinstance(row_data5, Tag): continue
                    if not isinstance(row_data6, Tag): continue
                    if not isinstance(row_data7, Tag): continue

                    player = Player()
                    if team_name is not None:
                        player.team = team_name
                    player.role = PlayerData[row_data[0].text]
                    
                    player.name = row_data1.select("a")[0].text
                    player.kda = Serialization.parse_str(row_data[2].text)
                    player.kp = Serialization.get_float(row_data[3].text)
                    player.vspm = Serialization.parse_str(row_data[4].text)
                    player.dmg = Serialization.get_float(row_data5.select("span")[0].text)
                    player.gold = Serialization.get_float(row_data6.select("span")[0].text)
                    champions = row_data7.find_all("span", class_="text-center")
                    matches_played = 0
                    for champion in champions:
                        if not isinstance(champion, Tag): continue
                        champion_name = str(champion.select("img")[0].get("alt"))
                        champion_text = champion.text
                        champion_played_list = champion_text.split("\n")
                        champion_played = champion_played_list[-1].strip()
                        player.add_champion(champion_name, champion_played)
                        matches_played += int(champion_played)
                    player.matches_played = matches_played
                    team.add_player(player.role, player)
            self.teams[team_name] = team
            print(f"Fetched team: {team_name}")
        try:
            print("Saving data...")
            with open("data/team_data.json", "w") as file:
                json.dump(self.teams, file, default=Serialization.encode_value)
        except Exception as e:
            print("Error saving data")
            print(e.args[0])
    
    @staticmethod
    def fetch_matches():
        page = DataService.fetch_data(leaguepedia_address)
        if page is None: return []

        headers = page.find_all(class_="frontpage-header")
        name_suffix = "logo std.png"
        result = []
        for header in headers:
            if not isinstance(header, Tag): continue
            if not header.string == "Matches & Results": continue

            container = header.find_next("div")
            if not isinstance(container, Tag): continue

            match_rows = container.find_all("tr")
            for row in match_rows:
                if not isinstance(row, Tag): continue

                match_data = row.find_all("td")
                if len(match_data) == 0:
                    continue
                
                match_data2 = match_data[2]
                match_data3 = match_data[3]
                if not isinstance(match_data2, Tag): continue
                if not isinstance(match_data3, Tag): continue

                team_data = match_data2.find_all(class_="mw-file-element")
                team_data0 = team_data[0]
                team_data1 = team_data[1]
                if not isinstance(team_data0, Tag): continue
                if not isinstance(team_data1, Tag): continue


                try:
                    team1_data = team_data0["data-image-name"]
                    team2_data = team_data1["data-image-name"]
                except Exception as e:
                    print("Match TBD")
                    continue

                team1 = str(unicodedata.normalize('NFKD', str(team1_data)).encode('ascii', 'ignore'))
                team1 = team1[2:team1.find(name_suffix)]
                offset1 = team1.find("(")
                if offset1 != -1:
                    team1 = team1[:offset1]
                team2 = str(unicodedata.normalize('NFKD', str(team2_data)).encode('ascii', 'ignore'))
                team2 = team2[2:team2.find(name_suffix)]
                offset2 = team2.find("(")
                if offset2 != -1:
                    team2 = team2[:offset2]
        
                countdown_data = match_data3.find(class_="countdowndate")
                if not isinstance(countdown_data, Tag): continue
                countdown_value = countdown_data.string
                if countdown_value is None: continue

                countdown_value = countdown_value[:countdown_value.find(" +")]
                countdown_date = datetime.strptime(countdown_value, "%d %b %Y %H:%M:%S")
                if countdown_date < datetime.now() + timedelta(hours=12):
                    result.append({
                        "team1": team1,
                        "team2": team2,
                    })
        return result

    def fetch_coefficients(self):
        print("Calculating coefficients...")
        request = {"season": "S15"}
        page = DataService.fetch_data_api(tournament_list_address, request)
        if page is None: return
        page_data = page.json()
        print(f"Found {len(page_data)} tournaments.")

        for tournament in page_data:
            tournament_name = tournament["trname"]
            tournament_stats_address = tournament_address + tournament_name + "/"
            tournament_page = DataService.fetch_data(tournament_stats_address)
            if tournament_page is None: continue
            tournament_data = tournament_page.find_all(class_="fond-main-cadre")
            tournament_data2 = tournament_data[2]
            if not isinstance(tournament_data2, Tag): continue

            tournament_table = tournament_data2.find("table", class_="table_list")
            if not isinstance(tournament_table, Tag): continue
            tournament_rows = tournament_table.find_all("tr")

            for row in tournament_rows:
                if not isinstance(row, Tag): continue
                victory = row.find("td", class_="text_victory")
                defeat = row.find("td", class_="text_defeat")
                if victory is None or defeat is None:
                    continue

                if not isinstance(victory, Tag) or not isinstance(defeat, Tag): continue
                
                if victory.sourcepos is None or defeat.sourcepos is None: continue
                winning_side_left = victory.sourcepos < defeat.sourcepos

                link = row.find("a")
                if link is None:
                    continue

                if not isinstance(link, Tag): continue
                link_address = link['href']
                link_address_items = str(link_address).split("/")
                link_address_items[4] = "page-summary"
                link_address = ""
                for item in link_address_items:
                    if item != "":
                        link_address += item + "/"
                
                match_page = DataService.fetch_data(golgg_address + link_address[2:])
                if not isinstance(match_page, Tag): continue
                
                winning_team = Team()
                losing_team = Team()

                victory_name = victory.string
                if victory_name is None: continue
                winning_team.name = victory_name

                defeat_name = defeat.string
                if defeat_name is None: continue
                losing_team.name = defeat_name

                gold_leads = match_page.find_all(class_="align-middle")
                for gold_lead in gold_leads:
                    if not isinstance(gold_lead, Tag): continue
                    gold_lead_data = gold_lead.find("span")
                    if not isinstance(gold_lead_data, Tag): continue
                    gold_lead_value = gold_lead_data.text
                    gold_lead_value = gold_lead_value.replace("+", "")
                    if gold_lead_value.find("k") != -1:
                        gold_lead_value = gold_lead_value.replace("k", "")
                        gold_lead_value = Serialization.parse_str(gold_lead_value) * 1000
                    else:
                        gold_lead_value = Serialization.parse_str(gold_lead_value)
                    if "left-side-win" in gold_lead.attrs['class'] and winning_side_left:
                        winning_team.gold_per_minute_or_gold_lead += int(gold_lead_value)
                    elif "right-side-win" in gold_lead.attrs['class'] and not winning_side_left:
                        winning_team.gold_per_minute_or_gold_lead += int(gold_lead_value)
                    else:
                        losing_team.gold_per_minute_or_gold_lead += int(gold_lead_value)

                team_stats_container = match_page.select("div.row.pt-4")
                team_stats = team_stats_container[0].find_all(class_="row")

                i = 0
                for team in team_stats:
                    if not isinstance(team, Tag): continue
                    stats_data = team.find_all(class_="score-box")
                    j = 0
                    for stat in stats_data:
                        if not isinstance(stat, Tag): continue
                        stat_value = stat.text
                        new_stat_value = ''.join(ch for ch in stat_value if ch.isdigit())
                        stat_value = Serialization.parse_str(new_stat_value)
                        if winning_side_left and i == 0:
                            setattr(winning_team, MatchData[j], stat_value)
                        elif not winning_side_left and i == 1:
                            setattr(winning_team, MatchData[j], stat_value)
                        else:
                            setattr(losing_team, MatchData[j], stat_value)
                        j += 1
                    i += 1

                player_stats = match_page.find_all(class_="table_list")
                
                i = 0
                for team in player_stats:
                    if not isinstance(team, Tag): continue
                    team_data = team.find_all("tr")
                    j = 0
                    for player_data in team_data:
                        if not isinstance(player_data, Tag): continue
                        team_header = player_data.find_all("th")
                        if team_header: continue
                        player_stat_data = player_data.find_all("td", class_="text-center")
                        player = Player()
                        if j > 4: continue # ? 6 players
                        player.role = CoefficientRoles[j]
                        k = 0
                        for stat in player_stat_data:
                            if not isinstance(stat, Tag): continue
                            stat_value = stat.string
                            if stat_value is None: continue
                            start_index = stat_value.find('(') + 1
                            end_index = stat_value.find(')')
                            if start_index == -1 or end_index == -1:
                                stat_value = Serialization.parse_str(stat_value)
                            else:
                                stat_value = stat_value[start_index:end_index]
                                stat_value = Serialization.parse_str(stat_value)
                            if stat_value == "-":
                                stat_value = 30.0
                            setattr(player, CoefficientPlayerAttributes[k], stat_value)
                            k += 1
                        if winning_side_left and i == 0:
                            setattr(winning_team, CoefficientRoles[j], player)
                        elif not winning_side_left and i == 1:
                            setattr(winning_team, CoefficientRoles[j], player)
                        else:
                            setattr(losing_team, CoefficientRoles[j], player)
                        j += 1
                    i += 1

                self.coefficients.evaluate_coefficients(winning_team, losing_team)
            print(f"Evaluated {tournament_name} ... Saving")
            try:
                with open("data/coefficient_data.json", "w") as file:
                    json.dump(self.coefficients, file, default=Serialization.encode_value)
            except Exception as e:
                print("Error saving data")
                print(e.args[0])

    def get_team(self, team_name):
        try:
            if team_name in self.teams:
                print(f"Found team: {team_name}")
                return self.teams[team_name]
            else:
                #print(f"Team {team_name} not found.")
                return
        except Exception as e:
            print("Error getting team")
            print(e.args[0])
            return

    def get_coefficients(self):
        return self.coefficients