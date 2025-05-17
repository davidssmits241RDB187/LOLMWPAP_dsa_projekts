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
        
   

    def evaluate_team1_vs_team2_default(self):
        # Compare float fields of the Team (excluding players)
        team1_dict = asdict(self.team1)
        team2_dict = asdict(self.team2)

        for key in team1_dict:
            

            val1 = team1_dict[key]
            val2 = team2_dict[key]

            self.evaluate_values(key, val1, val2)  # Pass key here!

        # Compare Player objects
        for role in ['top', 'jungle', 'mid', 'adc', 'support']:
            player1 = getattr(self.team1, role)
            player2 = getattr(self.team2, role)
            if player1 and player2:
                self.evaluate_values(None,player1, player2)


        print(f"{self.team1_name} score: {self.team1_evaluation} ========= {self.team2_name} score: {self.team2_evaluation}")


  
                
    def evaluate_values(self,key_for_coeff, value_for_team1, value_for_team2):
        
        #check if inputed value is a float value of the team object 
        if isinstance(value_for_team1, float) and isinstance(value_for_team2, float):
            
            coeff = self.coefficients.get(key_for_coeff, None)
            if coeff and isinstance(coeff, list) and len(coeff) == 2 and coeff[1] != 0:
                multiplier = coeff[0] / coeff[1]
            else:
                multiplier = 1.0 

            if value_for_team1 > value_for_team2:
                self.team1_evaluation += multiplier
                print(f"increased team1 by {multiplier} {key_for_coeff} {value_for_team1} {value_for_team2}")
            elif value_for_team1 < value_for_team2:
                self.team2_evaluation += multiplier
                print(f"increased team2 by {multiplier} {key_for_coeff} {value_for_team1} {value_for_team2}")

        #check if the inputed value is a player object of the team object
        #go through each of the player objects values and evaluate
        elif isinstance(value_for_team1, Player) and isinstance(value_for_team2, Player):
            
            player1_values = asdict(value_for_team1)
            player2_values = asdict(value_for_team2)

            for key in player1_values:
                val1 = player1_values[key]
                val2 = player2_values[key]
                if isinstance(val1, float) and isinstance(val2, float):
                    
                    role = value_for_team1.role
                    coeff_key = f"{role}_{key}"
                    coeff = self.coefficients.get(coeff_key, None)
                    if coeff and isinstance(coeff, list) and len(coeff) == 2 and coeff[1] != 0:
                        multiplier = coeff[0] / coeff[1]
                    else:
                        multiplier = 1.0

                    if val1 > val2:
                        value_for_team1.player_evaluation += multiplier
                        self.team1_evaluation += multiplier
                        print(f"increased team1 by {multiplier} {key} {value_for_team1} {value_for_team2}")
                    elif val1 < val2:
                        value_for_team2.player_evaluation += multiplier
                        self.team2_evaluation += multiplier
                        print(f"increased team2 by {multiplier} {key} {value_for_team1} {value_for_team2}")
                
                
                
            
            
            