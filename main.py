from controllers.match_controller import Match
from services.data_service import DataService
from functions.evaluate_function import evaluate_coefficients

def main():
    # * test data
    #data_service.fetch_coefficients()
    #data_service.fetch_teams()
    
    DS = DataService()
    
    matches = DS.fetch_matches()
    
    for match in matches:
        
        team1 = DS.get_team(match["team1"])
        team2 = DS.get_team(match["team2"])
        
        if team1 is None or team2 is None:
            continue

        match = Match(team1,team2,DS)
        match.evaluate_team1_vs_team2()
    while True:
        team1_name = str(input("Enter the first teams name: "))
        team2_name = str(input("Enter the second teams name: "))
        try:
            team1 = DS.get_team(team1_name)
            team2 = DS.get_team(team2_name)
            if team1 is None or team2 is None:
                print("Error getting teams")
                continue
            match = Match(team1, team2, DS)
            match.evaluate_team1_vs_team2()
        except Exception:
            print("Invalid input")
main()