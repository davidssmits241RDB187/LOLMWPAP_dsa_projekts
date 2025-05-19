

from functions.coefficient_file_management import write_match_to_file, read_matches_from_file
from services.data_service import DataService
from services.player_service import Player
from services.team_service import Team

def evaluate_coefficients(winning_team: Team,losing_team:Team):
        read_coefficients = read_matches_from_file()
       
        
        
        #kda csm dpm wpm
        #gold_lead kills towers dragons barons
        '''
        won higher [+1,0]
        won lower [0,0]
        lost higher [0,+1]
        lost lower [0,0]
        '''
        
        default_team_values_list = ["gold_per_minute_or_gold_lead", "kills_per_game","avg_tower_difference","dragons_per_game","nashor_per_game"]

        for x in range(5):
            try:
                win_value = getattr(winning_team,default_team_values_list[x])
                los_value = getattr(losing_team,default_team_values_list[x])
                
                if win_value > los_value:
                    getattr(read_coefficients,default_team_values_list[x])[0]+=1
                elif win_value < los_value:
                    getattr(read_coefficients,default_team_values_list[x])[1]+=1
            except Exception as e:
                pass
        
        roles = ["top", "jungle", "mid", "bot", "support"]
        player_attributes = ["csm", "dmg", "vspm","kda"]
       

        for i in range(5):
        
            winning_player = Player(**getattr(winning_team,roles[i]))
            losing_player = Player(**getattr(losing_team,roles[i]))
            
            for attribute in player_attributes:
                try:
                    win_val = getattr(winning_player, attribute)
                    lose_val = getattr(losing_player, attribute)
                
                    coeff = f"{roles[i]}_{player_attributes[player_attributes.index(attribute)]}"
                    if win_val > lose_val:
                        getattr(read_coefficients, coeff)[0] += 1
                    elif win_val < lose_val:
                        getattr(read_coefficients, coeff)[1] += 1
                except Exception as e:
                    pass
                
        
    
        write_match_to_file(read_coefficients)
    

