

class Player:
    def __init__(self, team, role, name, kda, kp, cspm, vspm, dmg, gold, champions_dictionary, champion_played):
        self.team = team
        self.role = role
        self.name = name
        
        self.kda = kda
        self.kp = kp
        self.cspm = cspm
        self.vspm = vspm
        self.dmg = dmg
        
        self.gold = gold
        
        self.champions_dictionary = champions_dictionary # champion name: win percentage (example-> janna:0.63)
        self.matches_played = 0
        self.player_evaluation = 0
        
class Team:
    def __init__(self):
        self.players = []
        self.gold_lead = 0
        self.average_game_duration = 0
        self.matches = 0
        self.side_winrates = [0,0]
        self.team_evaluation = 0
        '''
        self.top_laners = []
        self.junglers=[]
        self.mid_laners = []
        self.adcs=[]
        self.supports = []
        for player in self.players:
            Role = player.role
            match Role:
                case "top":
                    self.top_laners.append(player)
                case "jungler":
                    self.junglers.append(player)
                case "mid":
                    self.mid_laners.append(player)
                case "adc":
                    self.adcs.append(player)
                case "support":
                    self.supports.append(player)
        '''
        
       
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
            player.self_evaluation += player.kda + player.kp + player.cspm + player.vspm + player.dmg
            
    
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

    def evaluate_team1_vs_team2(self):
        pass
            
            

    
                    