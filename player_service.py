from team_service import Team

from dataclasses import dataclass

@dataclass
class Player:
    team: Team
    role: str
    name: str
    kda: float
    kp: float
    vspm: float
    dmg: float
    gold: float
    cspm: float
    champions_dictionary: dict
    matches_played: int = 0
    player_evaluation: float = 0.0