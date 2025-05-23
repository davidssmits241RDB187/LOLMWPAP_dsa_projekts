from classes.player import Player

from dataclasses import dataclass

@dataclass
class Team:
    name:                           str = ""
    region:                         str = ""
    season:                         str = ""
    winrate:                        str = ""
    _winrate:                       float = 0.0
    game_duration:                  float = 0.0
    gold_per_minute_or_gold_lead:   int = 0
    gold_differential_per_minute:   int = 0
    gold_differential_at_15_min:    int = 0
    _winrate_at_15_min:             float = 0.0
    cspm:                           float = 0.0
    cs_differential_at_15_min:      int = 0
    tower_differential_at_15_min:   float = 0.0
    avg_tower_difference:           float = 0.0
    _first_tower:                   float = 0.0
    damage_per_minute:              int = 0
    _first_blood:                   float = 0.0
    kills_per_game:                 float = 0.0
    deaths_per_game:                float = 0.0
    avg_kd:                         float = 0.0
    avg_ak:                         float = 0.0
    plates_per_game:                float = 0.0
    dragons_per_game:               float = 0.0
    dragons_at_15_min:              float = 0.0
    void_grubs_per_game:            float = 0.0
    atakhan_per_game:               float = 0.0
    herald_per_game:                float = 0.0
    nashor_per_game:                float = 0.0
    _feats_of_strength:             float = 0.0
    vision_score_per_minute:        float = 0.0
    wards_per_minute:               float = 0.0
    vision_wards_per_minute:        float = 0.0
    wards_cleared_per_minute:       float = 0.0
    _wards_cleared:                 float = 0.0
    #players
    top:        Player | None = None
    jungle:     Player | None = None
    mid:        Player | None = None
    bot:        Player | None = None
    support:    Player | None = None

    def add_player(self, player_role: str, player: Player):
        
        if getattr(self,player_role) is None:
            
            setattr(self, player_role, player)
        
        

