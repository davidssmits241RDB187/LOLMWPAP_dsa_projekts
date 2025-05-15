from classes_folder.team_classes_folder.team_service import Team


from dataclasses import dataclass, field

@dataclass
class Player:
    team:                   Team = None
    role:                   str = ""
    name:                   str = ""
    kda:                    float = 0.0
    kp:                     float = 0.0
    vspm:                   float = 0.0
    dmg:                    float = 0.0
    gold:                   float = 0.0
    cspm:                   float = 0.0
    champions_dictionary: dict = field(default_factory=dict)
    matches_played:         int = 0
    player_evaluation:      float = 0.0