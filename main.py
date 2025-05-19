from controllers.match_controller import MatchController
from services.data_service import DataService

import os

def main():
    DS = DataService()
    
    while True:
        os.system("cls||clear")
        print("""
    ================== Choose action: ====================
        0 - compare teams
        1 - compare upcoming matches (12h)
        2 - fetch coefficient data (can be stopped)
        3 - fetch team data
        4 - close
    ======================================================
        """)
        print("Enter your action: ", end="")
        user_input = input()

        match user_input:
            case "0":
                os.system("cls||clear")
                team1_name = str(input("Enter the first teams name: "))
                team2_name = str(input("Enter the second teams name: "))

                try:
                    team1 = DS.get_team(team1_name)
                    team2 = DS.get_team(team2_name)
                    if team1 is None or team2 is None:
                        print("Teams not found")
                        continue
                    
                    match = MatchController(team1, team2, DS)
                    match.evaluate_team1_vs_team2()
                except Exception:
                    print("Invalid input")
                input("Input key to continue...")
                
            case "1":
                os.system("cls||clear")
                matches = DS.fetch_matches()

                for match in matches:
                    team1 = DS.get_team(match["team1"])
                    team2 = DS.get_team(match["team2"])
                    if team1 is None or team2 is None:
                        print("Teams not found")
                        continue

                    match = MatchController(team1, team2, DS)
                    match.evaluate_team1_vs_team2()
                input("Input key to continue...")

            case "2":
                os.system("cls||clear")
                DS.fetch_coefficients()
                input("Input key to continue...")

            case "3":
                os.system("cls||clear")
                DS.fetch_teams()
                input("Input key to continue...")

            case "4":
                break
main()