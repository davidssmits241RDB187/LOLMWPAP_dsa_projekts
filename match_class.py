from dataclasses import asdict



class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.history = [0,0]
        self.top_coefficient = 1
        self.jungle_coefficient = 1
        self.mid_coefficient = 1 
        self.adc_coefficient = 1
        self.support_coefficient = 1

    def evaluate_team1_vs_team2_default(self):
        team1_values = asdict(self.team1.default_team_values) 
        team2_values = asdict(self.team2.default_team_values)
        for key in team1_values:
            self.evaluate_values(team1_values[key],team2_values[key])
        
            
    def evaluate_values(self,value_for_team1, value_for_team2):
        if value_for_team1>value_for_team2:
            self.team1.team_evaluation+=1
        elif value_for_team1<value_for_team2:
            self.team2.team_evaluation+=1