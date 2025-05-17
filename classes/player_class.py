from dataclasses import dataclass, field, asdict
from coefficients_class import Coefficients
from teams_class import Team
from coefficient_file_management import write_match_to_file, read_matches_from_file
from match_class import Match
class Player:
    def __init__(self, team:Team, role:str, name:str, kda:float, kp:float, cspm:float, vspm:float, dmg:float, gold:float, champions_dictionary:dict, champion_played:str):
        self.team = team
        self.role = role
        self.name = name
        
        self.kda = kda
        self.kp = kp
        self.vspm = vspm
        
        #!gol gg team statistics returns dmg and gold as percentages, which will not work with evaluation
        #!only use these in individual match analysis
        self.dmg = dmg
        self.gold = gold
        self.cspm = cspm
        #!
        
        self.champions_dictionary = champions_dictionary # champion name: win percentage (example-> janna:0.63)
        self.matches_played = 0
        self.player_evaluation = self.kda + self.kp + self.cspm + self.vspm + self.dmg