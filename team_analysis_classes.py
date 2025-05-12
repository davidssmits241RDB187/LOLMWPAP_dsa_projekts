

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
        self.player_evaluation += self.kda + self.kp + self.cspm + self.vspm + self.dmg
        
class Team:
    def __init__(self,players):
        
        #!this section is for live game analysis, not essential!
        self.dragon_priority = {} #example {cloud: [11, 6], ocean: [8, 12]} first in list is killed, second in list is lost
        self.average_game_duration = 0
        self.side_winrates = [0,0]
        #!
        
        self.winrate = 0
        
        self.gold_per_minute = 0
        self.gold_differential_per_minute = 0
        self.gold_differential_at_15_min = 0
        self.cspm = 0
        self.cs_differential_at_15_min = 0
        self.tower_differential_at_15_min = 0
        self.avg_tower_difference = 0
        self.first_tower = 0
        
        self.damage_per_minute = 0
        self.first_blood = 0
        self.kills_per_game = 0
        self.deaths_per_game = 0
        self.avg_kd = 0
        
        self.plates_per_game = 0
        self.plates_per_game_per_side = {} # example top:1.2, mid:0.7
        self.dragons_per_game = 0
        self.dragons_at_15_min = 0
        self.void_grubs_per_game = 0
        self.atakhan_per_game = 0
        self.herald_per_game = 0
        self.nashor_per_game = 0
        self.feats_of_strength = 0
        
        self.vision_score_per_minute = 0
        
        self.players = players
        self.team_evaluation = 0
        self.matches = 0
        self.top_laner = None
        self.jungler = None
        self.mid_laner = None
        self.adc = None
        self.support = None
        for player in self.players:
            Role = player.role
            match Role:
                case "top":
                    self.top_laner = player
                case "jungle":
                    self.jungler = player
                case "mid":
                    self.mid_laner = player
                case "bot":
                    self.adc = player
                case "support":
                    self.support = player
        
        
    #!prototype for individual match analysis, not essential!
    def evaluate_team_match_and_tournament(self,tournament_name, tournament_kills,gold_lead,match_players):
        match_coefficient = 1
        
        if tournament_name in []: # 2nd tier leagues
            match_coefficient = 1
        elif tournament_name in []: # 1st tier leagues
            match_coefficient = 2 # is changable
            
        self.gold_lead += (1/gold_lead) * match_coefficient
        
        for player in match_players: # maybe change to go through each role and use role coefficients
            player.matches_played += 1
            player.kda += player.kda*match_coefficient
            player.kp += (player.kda/tournament_kills)*match_coefficient # maybe dividing with zero
            player.cspm += player.cspm*match_coefficient
            player.vspm += player.vspm*match_coefficient
            player.dmg += player.dmg*match_coefficient
            player.player_evaluation += player.kda + player.kp + player.cspm + player.vspm + player.dmg
    #!     
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
        if self.team1.top_laner.player_evaluation > self.team2.top_laner.player_evaluation:
            self.team1.team_evaluation += 1*self.top_coefficient
        
            
            

    
                    