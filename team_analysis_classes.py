from dataclasses import dataclass,field

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
        


@dataclass
class DefaultTeamValues:
    winrate: dict[str, float] = field(default_factory=dict)
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
    plates_per_game_per_side: dict[str,float]= field(default_factory=dict)
    dragons_per_game:float
    dragons_at_15_min:float
    void_grubs_per_game:float
    atakhan_per_game:float
    herald_per_game:float
    nashor_per_game:float
    feats_of_strength:float
    
    vision_score_per_minute:float
    
    
@dataclass
class Coefficients:
    gold_lead: list[float] = field(default_factory=lambda: [1.0, 1.0])
    kills: list[float] = field(default_factory=lambda: [1.0, 1.0])
    towers: list[float] = field(default_factory=lambda: [1.0, 1.0])
    dragons: list[float] = field(default_factory=lambda: [1.0, 1.0])
    barons: list[float] = field(default_factory=lambda: [1.0, 1.0])
    
    top_kda: list[float] = field(default_factory=lambda: [1.0, 1.0])
    top_csm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    top_dpm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    top_wpm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    
    mid_kda: list[float] = field(default_factory=lambda: [1.0, 1.0])
    mid_csm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    mid_dpm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    mid_wpm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    
    jungle_kda: list[float] = field(default_factory=lambda: [1.0, 1.0])
    jungle_csm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    jugnle_dpm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    jungle_wpm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    
    bot_kda: list[float] = field(default_factory=lambda: [1.0, 1.0])
    bot_csm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    bot_dpm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    bot_wpm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    
    support_kda: list[float] = field(default_factory=lambda: [1.0, 1.0])
    support_csm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    support_dpm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    support_wpm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    
    

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
    
    
    
def evaluate_coefficients(self,winning_team,losing_team,read_coefficients):
       i = 0
       #kda csm dpm vpm
       while i < 5:
           if winning_team.players[i].kda>losing_team.players[i].kda:
                if winning_team.players[i].role == "top":
                   read_coefficients.top_kda[0] += 1
                elif winning_team.players[i].role == "jungle":
                   read_coefficients.jungle_kda[0] += 1
                elif winning_team.players[i].role == "mid":
                   read_coefficients.mid_kda[0] += 1
                elif winning_team.players[i].role == "mid":
                   read_coefficients.mid_kda[0] += 1
                elif winning_team.players[i].role == "bot":
                   read_coefficients.bot_kda[0] += 1
                elif winning_team.players[i].role == "support":
                   read_coefficients.support_kda[0] += 1
           i += 1
           
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
        pass
            
    def evaluate_values(self,value_for_team1, value_for_team2):
        if value_for_team1>value_for_team2:
            self.team1.team_evaluation+=1
        elif value_for_team1<value_for_team2:
            self.team2.team_evaluation+=1
            
            
    
            
            

    
                    