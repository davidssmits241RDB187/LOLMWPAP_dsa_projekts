
from functions.evaluate_function import evaluate_coefficients
from classes.match_class import Match
from functions.coefficient_file_management import write_match_to_file,read_matches_from_file
from classes.coefficients_class import Coefficients
from services.data_service import DataService

def main():
    # * test data
    print("Testing data service")
    
    data_service = DataService()
    data_service.fetch_coefficients()
    #data_service.fetch_teams()
    #match1 = Match("T1", "Los Ratones")
    #match1.evaluate_team1_vs_team2_default()

    #evaluate_coefficients( "DMG Esports","T1")
    #evaluate_coefficients("G2 Esports", "T1")
    
    #match2 = Match("Los Ratones", "NORD Esports")
    #match2.evaluate_team1_vs_team2_default()
main()