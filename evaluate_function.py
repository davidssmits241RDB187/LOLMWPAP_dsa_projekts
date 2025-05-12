


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
                elif winning_team.players[i].role == "bot":
                   read_coefficients.bot_kda[0] += 1
                elif winning_team.players[i].role == "support":
                   read_coefficients.support_kda[0] += 1
           i += 1