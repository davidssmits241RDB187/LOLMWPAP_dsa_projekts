from dataclasses import dataclass

@dataclass
class Team:
    team_name:                      str = None
    season:                         str = None
    region:                         str = None
    games:                          int = 0
    winrate:                        float = 0.0
    avg_kd:                         float = 0.0
    gold_per_minute_or_gold_lead:   float = 0.0
    gold_differential_per_minute:   float = 0.0
    game_duration:                  float = 0.0
    kills_per_game:                 float = 0.0
    deaths_per_game:                float = 0.0
    towers_killed:                  float = 0.0
    towers_lost:                    float = 0.0
    first_blood:                    float = 0.0
    first_tower:                    float = 0.0
    feats_of_strength:              float = 0.0
    dragons_per_game:               float = 0.0
    dragons_percent:                float = 0.0
    void_grubs_per_game:            float = 0.0
    herald_per_game:                float = 0.0
    atakhan_per_game:               float = 0.0
    dragons_at_15_min:              float = 0.0
    tower_differential_at_15_min:   float = 0.0
    gold_differential_at_15_min:    float = 0.0
    avg_tower_difference:           float = 0.0
    nashor_per_game:                float = 0.0
    nash_percent:                   float = 0.0
    cspm:                           float = 0.0
    damage_per_minute:              float = 0.0
    wards_per_minute:               float = 0.0
    vision_wards_per_minute:        float = 0.0
    cleared_wards_per_minute:       float = 0.0