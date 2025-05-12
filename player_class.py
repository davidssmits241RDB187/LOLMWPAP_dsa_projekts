from dataclasses import dataclass, field, asdict

class Player:
    def __init__(self, team, role, name, kda, kp, cspm, vspm, dmg, gold, champions_dictionary, champion_played):
        self.team = team
        self.role = role
        self.name = name
        
        self.kda = kda
        self.kp = kp
        self.cspm = cspm
        self.vspm = vspm
        
        #!gol gg team statistics returns dmg and gold as percentages, which will not work with evaluation
        #!only use these in individual match analysis
        self.dmg = dmg
        self.gold = gold
        #!
        
        self.champions_dictionary = champions_dictionary # champion name: win percentage (example-> janna:0.63)
        self.matches_played = 0
        self.player_evaluation = self.kda + self.kp + self.cspm + self.vspm + self.dmg