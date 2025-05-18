from controllers.match_controller import Match

def main():
    # * test data
    #data_service.fetch_coefficients()
    #data_service.fetch_teams()
    match1 = Match("T1", "Los Ratones")
    match1.evaluate_team1_vs_team2()
main()