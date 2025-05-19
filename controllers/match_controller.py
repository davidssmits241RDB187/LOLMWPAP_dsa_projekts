from services.data_service import DataService
from classes.player import Player
from classes.team import Team

from dataclasses import asdict

class MatchController:
    def __init__(self, team1:Team, team2:Team, DS: DataService):
        self.DS = DS
        self.team1 = team1
        self.team2 = team2
        self.team1_evaluation = 0
        self.team2_evaluation = 0
        self.history = [0,0]

    def dict_to_player(self,player_dict):
        return Player(**player_dict)
    
    def evaluate_team1_vs_team2(self):
        
        team1_dict = asdict(self.team1)
        team2_dict = asdict(self.team2)
        print(f"Evaluating {self.team1.name} vs {self.team2.name}...")
        for key in team1_dict:
            
            
            val1 = team1_dict[key]
            val2 = team2_dict[key]

            self.evaluate_values(key, val1, val2)  
            
        print(f"{self.team1.name} score: {self.team1_evaluation} ========= {self.team2.name} score: {self.team2_evaluation}")
    
    def evaluate_values(self, key_for_coeff, value_for_team1, value_for_team2):
        try:
            if isinstance(value_for_team1, str) and isinstance(value_for_team2, str):
                value_for_team1 = float(value_for_team1)
                value_for_team2 = float(value_for_team2)
            elif isinstance(value_for_team1, dict) and isinstance(value_for_team2, dict):
                value_for_team1 = Player(**value_for_team1)
                value_for_team2 = Player(**value_for_team2)
        except Exception as e:
            pass
            
        if isinstance(value_for_team1, (float, int)) and isinstance(value_for_team2, (float, int)):
            coeff = getattr(self.DS.coefficients, key_for_coeff, None)

            if coeff and isinstance(coeff, list) and len(coeff) == 2 and coeff[1] != 0:
                multiplier = coeff[0] / coeff[1]
               
            else:
                multiplier = 1.0
            
            if value_for_team1 > value_for_team2:
                self.team1_evaluation += multiplier
                
            elif value_for_team1 < value_for_team2:
                self.team2_evaluation += multiplier
                
            return

        
        if isinstance(value_for_team1, Player) and isinstance(value_for_team2, Player):
            
            player1_values = asdict(value_for_team1)
            player2_values = asdict(value_for_team2)

            for subkey in player1_values:
                val1 = player1_values[subkey]
                val2 = player2_values[subkey]
                try:
                    if isinstance(val1, str) and isinstance(val2, str):
                        val1 = float(val1)
                        val2 = float(val2)
               
                except Exception as e:
                    pass
                    
                if isinstance(val1, (float, int)) and isinstance(val2, (float, int)):
                    coeff_key = f"{value_for_team1.role}_{subkey}"
                    coeff = getattr(self.DS.coefficients, coeff_key, None)

                    if coeff and isinstance(coeff, list) and len(coeff) == 2 and coeff[1] != 0:
                        multiplier = coeff[0] / coeff[1]
                        
                    else:
                        multiplier = 1.0
                    
                    if val1 > val2:
                        self.team1_evaluation += multiplier
                       
                    elif val1 < val2:
                        self.team2_evaluation += multiplier
                        