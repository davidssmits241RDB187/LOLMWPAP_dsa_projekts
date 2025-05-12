from player_class import Player
from coefficients_class import Coefficients
from dataclasses import dataclass
@dataclass
class DefaultTeamValues:
    winrate: float
    gold_per_minute: float
    gold_differential_per_minute:float
    gold_differential_at_15_min:float
    cspm:float
    cs_differential_at_15_min:float
    tower_differential_at_15_min:float
    avg_tower_difference:float
    first_tower:float
    
    damage_per_minute:float
    first_blood:float
    kills_per_game:float
    deaths_per_game:float
    avg_kd:float
    
    plates_per_game:float
    plates_per_game_per_side: float
    dragons_per_game:float
    dragons_at_15_min:float
    void_grubs_per_game:float
    atakhan_per_game:float
    herald_per_game:float
    nashor_per_game:float
    feats_of_strength:float
    
    vision_score_per_minute:float


class Team:
    def __init__(self,players,winrate,gold_per_minute,gold_differential_per_minute, gold_differential_at_15_min, cspm, cs_differential_at_15_min,tower_differential_at_15_min, avg_tower_difference, first_tower, damage_per_minute, first_blood,kills_per_game,deaths_per_game,avg_kd,plates_per_game,plates_per_game_per_side,dragons_per_game,dragons_at_15_min,void_grubs_per_game,atakhan_per_game,herald_per_game,nashor_per_game,feats_of_strength):
        
        #!this section is for live game analysis, not essential!
        self.dragon_priority = {} #example {cloud: [11, 6], ocean: [8, 12]} first in list is killed, second in list is lost
        self.average_game_duration = 0
        self.side_winrates = [0,0]
        #!
        
        self.default_team_values = DefaultTeamValues(winrate,gold_per_minute,gold_differential_per_minute,gold_differential_at_15_min,)
    
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
   