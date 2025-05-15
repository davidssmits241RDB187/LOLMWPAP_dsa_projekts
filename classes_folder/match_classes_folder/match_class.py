from dataclasses import asdict
from classes_folder.team_classes_folder.team_service import Team
from functions_folder.coefficients_functions_folder.coefficient_file_management import read_matches_from_file
from classes_folder.player_classes_folder.player_service import Player
class Match:
    def __init__(self, team1:Team, team2:Team):
        self.team1 = team1
        self.team2 = team2
        self.history = [0,0]
        self.coefficients = asdict(read_matches_from_file())

    def evaluate_team1_vs_team2_default(self):
        team1_values = asdict(self.team1) 
        team2_values = asdict(self.team2)
        for key in team1_values:
            self.evaluate_values(key,team1_values[key],team2_values[key])
        
            
    def evaluate_values(self, key, value_for_team1, value_for_team2):
        
        #check if inputed value is a float value of the team object
        if isinstance(value_for_team1, float) and isinstance(value_for_team2, float):
            
            coeff = self.coefficients.get(key, None)
            if coeff and isinstance(coeff, list) and len(coeff) == 2 and coeff[1] != 0:
                multiplier = coeff[0] / coeff[1]
            else:
                multiplier = 1.0 

            if value_for_team1 > value_for_team2:
                self.team1.team_evaluation += multiplier
            elif value_for_team1 < value_for_team2:
                self.team2.team_evaluation += multiplier

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
                        self.team1.team_evaluation += multiplier
                    elif val1 < val2:
                        value_for_team2.player_evaluation += multiplier
                        self.team2.team_evaluation += multiplier

                
                
                
                
            
            
            