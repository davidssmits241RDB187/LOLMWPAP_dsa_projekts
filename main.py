
from functions.evaluate_function import evaluate_coefficients
from classes.match_class import Match
from functions.coefficient_file_management import write_match_to_file,read_matches_from_file
from classes.coefficients_class import Coefficients
def main():
    # * test data
    print("Testing data service")
    
    match1 = Match("T1", "Los Ratones")
    match1.evaluate_team1_vs_team2_default()
    

    evaluate_coefficients("T1", "Los ratones")
    
    match1.evaluate_team1_vs_team2_default()
main()