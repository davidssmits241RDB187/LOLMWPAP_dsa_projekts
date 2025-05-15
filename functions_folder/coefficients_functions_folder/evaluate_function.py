
from classes_folder.team_classes_folder.team_service import Team
from functions_folder.coefficients_functions_folder.coefficient_file_management import write_match_to_file, read_matches_from_file


def evaluate_coefficients(winning_team:Team,losing_team:Team):
        read_coefficients = read_matches_from_file("coefficients.txt")
        
        
        #kda csm dpm wpm
        #gold_lead kills towers dragons barons
        '''
        won higher [+1,0]
        won lower [0,0]
        lost higher [0,+1]
        lost lower [0,0]
        '''
        
        default_team_values_list = ["gold_per_minute_or_gold_lead", "kills_per_game","avg_tower_difference","dragons_per_game_or_match","nashor_per_game"]
        team_coeffs = ["gold_lead","kills","towers","dragons","barons"]
        for x in range(5):
            
            win_value = getattr(winning_team,default_team_values_list[x])
            los_value = getattr(losing_team,default_team_values_list[x])
            if win_value > los_value:
                getattr(read_coefficients,team_coeffs[x])[0]+=1
            elif win_value < los_value:
                getattr(read_coefficients,team_coeffs[x])[1]+=1
        
        roles = ["top", "jungle", "mid", "bot", "support"]
        player_attributes = ["kda", "cspm", "dmg", "vspm"]
        players_coeffs = ["kda", "csm", "dpm", "wpm"]

        for i in range(5):
            winning_player = getattr(winning_team,roles[i])
            losing_player = getattr(losing_team,roles[i])
            for attribute in player_attributes:
                win_val = getattr(winning_player, attribute)
                lose_val = getattr(losing_player, attribute)
                coeff = f"{roles[i]}_{players_coeffs[player_attributes.index(attribute)]}"
                if win_val > lose_val:
                    getattr(read_coefficients, coeff)[0] += 1
                elif win_val < lose_val:
                    getattr(read_coefficients, coeff)[1] += 1

            
        write_match_to_file(read_coefficients)