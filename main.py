
from services.data_service import DataService
from classes.match_class import Match

def main():
    # * test data
    print("Testing data service")
    
    data_service = DataService()
    data_service.fetch_coefficients()
    #data_service.fetch_teams()
    #match1 = Match("T1", "Los Ratones")
    #match1.evaluate_team1_vs_team2_default()

main()