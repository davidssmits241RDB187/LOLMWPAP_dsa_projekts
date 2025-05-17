from dataclasses import dataclass, field, asdict

@dataclass
class Player:
    team:                   str = ""
    role:                   str = ""
    name:                   str = ""
    kda:                    float = 0.0
    kp:                     float = 0.0
    vspm:                   float = 0.0
    dmg:                    float = 0.0
    gold:                   float = 0.0
    champions:              dict = field(default_factory=dict)
    matches_played:         int = 0
    player_evaluation:      float = 0.0

    def add_champion(self, champion_name: str, matches_played: int):
        if champion_name in self.champions:
            self.champions[champion_name] += matches_played
        else:
            self.champions[champion_name] = matches_played
            
            
