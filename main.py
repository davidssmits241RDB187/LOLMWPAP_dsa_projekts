
from services.data_service import DataService
from classes.match_class import Match

def main():
    # * test data
    print("Testing data service")
    
    match1 = Match("100 Thieves", "A One Man Army")
    match1.evaluate_team1_vs_team2_default()

main()