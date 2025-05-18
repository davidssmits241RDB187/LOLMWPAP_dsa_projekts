RowData = {
    "Region : " : "region",
    "Season : " : "season",
    "Win Rate : " : "winrate",
    "%WinRate": "_winrate",
    "Average game duration : ": "game_duration",
    "Gold Per Minute:": "gold_per_minute_or_gold_lead",
    "Gold Differential per Minute:": "gold_differential_per_minute",
    "Gold Differential at 15 min:": "gold_differential_at_15_min",
    "Win Rate when ahead at 15 min:": "_winrate_at_15_min",
    "CS Per Minute:": "cspm",
    "CS Differential at 15 min:": "cs_differential_at_15_min",
    "Tower Differential at 15 min:": "tower_differential_at_15_min",
    "Avg. Tower Difference:": "avg_tower_difference",
    "First Tower :": "_first_tower",
    "Damage Per Minute:": "damage_per_minute",
    "First Blood:": "_first_blood",
    "Kills Per Game:": "kills_per_game",
    "Deaths Per Game:": "deaths_per_game",
    "Average Kill / Death Ratio:": "avg_kd",
    "Average Assists / Kill:": "avg_ak",
    "Plates / game (TOP|MID|BOT):": "plates_per_game",
    "Dragons / game:": "dragons_per_game",
    "Dragons at 15 min:": "dragons_at_15_min",
    "Voidgrubs / game:": "void_grubs_per_game",
    "Atakhan / game:": "atakhan_per_game",
    "Herald / game:": "herald_per_game",
    "Nashors / game:": "nashor_per_game",
    "Feats of Strength:": "_feats_of_strength",
    "Vision Score Per Minute:": "vision_score_per_minute",
    "Wards Per Minute:": "wards_per_minute",
    "Vision Wards Per Minute:": "vision_wards_per_minute",
    "Wards Cleared Per Minute:": "wards_cleared_per_minute",
    "% Wards Cleared:": "_wards_cleared",
}

PlayerData = {
    " TOP" : "top",
    " JUNGLE" : "jungle",
    " MID" : "mid",
    " BOT" : "bot",
    " SUPPORT" : "support",
}

CoefficientValues = [
    "gold_per_minute_or_gold_lead",
    "kills_per_game",
    "avg_tower_difference",
    "dragons_per_game",
    "nashor_per_game"
]

CoefficientCoeffs = [
    "gold_lead",
    "kills",
    "towers",
    "dragons",
    "barons"
]

CoefficientRoles = [
    "top",
    "jungle",
    "mid",
    "bot",
    "support"
]
    
CoefficientPlayerAttributes = [
    "kda", 
    #"cspm",
    "dmg",
    "vspm"
]
    
CoefficientPlayerCoeffs = [
    "kda",
    #"csm",
    "dpm",
    "wpm"
]