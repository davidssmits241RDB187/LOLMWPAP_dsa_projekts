from dataclasses import asdict
from team_service import Team
from coefficient_file_management import read_coeffs_from_file

class Match:
    def __init__(self, team1:Team, team2:Team):
        self.team1 = team1
        self.team2 = team2
        self.history = [0,0]
        
        self.coefficients = asdict(read_coeffs_from_file())

    def evaluate_team1_vs_team2_default(self):
        team1_values = asdict(self.team1) 
        team2_values = asdict(self.team2)
        for key in team1_values:
            self.evaluate_values(key,team1_values[key],team2_values[key])

            
    def evaluate_values(self,key,value_for_team1, value_for_team2):
        roles = ["top","jungle","mid","bot","support"]
        player_attributes = ["kda", "cspm", "dmg", "vspm"]
        players_coeffs = ["kda", "csm", "dpm", "wpm"]
        
        default_team_values_list = ["gold_per_minute_or_gold_lead", "kills_per_game","avg_tower_difference","dragons_per_game_or_match","nashor_per_game"]
        team_coeffs = ["gold_lead","kills","towers","dragons","barons"]
    
    
    
        #need to check if value is of team value or teams player value, then evaluate with corresponding coefficient
        if value_for_team1>value_for_team2:
            self.team1.team_evaluation+=1
        elif value_for_team1<value_for_team2:
            self.team2.team_evaluation+=1