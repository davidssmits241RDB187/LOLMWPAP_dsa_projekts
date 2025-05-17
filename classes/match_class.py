from dataclasses import asdict
from services.team_service import Team
from functions.coefficient_file_management import read_matches_from_file
from services.player_service import Player
from services.data_service import DataService
class Match:
    def __init__(self, team1_name, team2_name):
        DS = DataService()
        self.team1_name = team1_name
        self.team2_name = team2_name
        self.team1 = DS.get_team(team1_name)
        self.team2 = DS.get_team(team2_name)
        self.team1_evaluation = 0
        self.team2_evaluation = 0
        self.history = [0,0]
        self.coefficients = asdict(read_matches_from_file())
    
    def dict_to_player(self,player_dict):
        return Player(**player_dict)


    def evaluate_team1_vs_team2_default(self):
        
        team1_dict = vars(self.team1)
        team2_dict = vars(self.team2)

        for key in team1_dict:
            

            val1 = team1_dict[key]
            val2 = team2_dict[key]

            self.evaluate_values(key, val1, val2)  
            
        print(f"{self.team1_name} score: {self.team1_evaluation} ========= {self.team2_name} score: {self.team2_evaluation}")


    

                
    def evaluate_values(self, key_for_coeff, value_for_team1, value_for_team2):

        
        try:
            if isinstance(value_for_team1, str) and isinstance(value_for_team2, str):
                value_for_team1 = float(value_for_team1)
                value_for_team2 = float(value_for_team2)
            elif isinstance(value_for_team1, dict) and isinstance(value_for_team2, dict):
                value_for_team1 = Player(**value_for_team1)
                value_for_team2 = Player(**value_for_team2)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
            
       
        if isinstance(value_for_team1, (float, int)) and isinstance(value_for_team2, (float, int)):
            coeff = self.coefficients.get(key_for_coeff, None)
            if coeff and isinstance(coeff, list) and len(coeff) == 2 and coeff[1] != 0:
                multiplier = coeff[0] / coeff[1]
            else:
                multiplier = 1.0

            if value_for_team1 > value_for_team2:
                self.team1_evaluation += multiplier
                print(f"increased team1 by {multiplier} for {key_for_coeff}: {value_for_team1} > {value_for_team2}")
            elif value_for_team1 < value_for_team2:
                self.team2_evaluation += multiplier
                print(f"increased team2 by {multiplier} for {key_for_coeff}: {value_for_team1} < {value_for_team2}")
            return

        
        if isinstance(value_for_team1, Player) and isinstance(value_for_team2, Player):
            print(f"Evaluating Player objects for role: {value_for_team1.role}")
            player1_values = asdict(value_for_team1)
            player2_values = asdict(value_for_team2)

            for subkey in player1_values:
                val1 = player1_values[subkey]
                val2 = player2_values[subkey]
                try:
                    if isinstance(value_for_team1, str) and isinstance(value_for_team2, str):
                        value_for_team1 = float(value_for_team1)
                        value_for_team2 = float(value_for_team2)
               
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
                    
                if isinstance(val1, (float, int)) and isinstance(val2, (float, int)):
                    coeff_key = f"{value_for_team1.role}_{subkey}"
                    coeff = self.coefficients.get(coeff_key, None)
                    if coeff and isinstance(coeff, list) and len(coeff) == 2 and coeff[1] != 0:
                        multiplier = coeff[0] / coeff[1]
                    else:
                        multiplier = 1.0

                    if val1 > val2:
                        self.team1_evaluation += multiplier
                        print(f"increased team1 by {multiplier} for {coeff_key}: {val1} > {val2}")
                    elif val1 < val2:
                        self.team2_evaluation += multiplier
                        print(f"increased team2 by {multiplier} for {coeff_key}: {val1} < {val2}")
                else:
                    print(f"Skipping player subkey {subkey}: not float/int ({type(val1)})")
            return

       
