from dataclasses import dataclass, field
from classes.teams_class import Team
from functions.coefficient_file_management import write_match_to_file, read_matches_from_file
from classes.match_class import Match
from classes.player_class import Player
@dataclass
class Coefficients:
    
    gold_lead: list[float] = field(default_factory=lambda: [1.0, 1.0])
    kills: list[float] = field(default_factory=lambda: [1.0, 1.0])
    towers: list[float] = field(default_factory=lambda: [1.0, 1.0])
    dragons: list[float] = field(default_factory=lambda: [1.0, 1.0])
    barons: list[float] = field(default_factory=lambda: [1.0, 1.0])
    
    top_kda: list[float] = field(default_factory=lambda: [1.0, 1.0])
    top_csm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    top_dpm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    top_wpm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    
    mid_kda: list[float] = field(default_factory=lambda: [1.0, 1.0])
    mid_csm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    mid_dpm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    mid_wpm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    
    jungle_kda: list[float] = field(default_factory=lambda: [1.0, 1.0])
    jungle_csm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    jungle_dpm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    jungle_wpm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    
    bot_kda: list[float] = field(default_factory=lambda: [1.0, 1.0])
    bot_csm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    bot_dpm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    bot_wpm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    
    support_kda: list[float] = field(default_factory=lambda: [1.0, 1.0])
    support_csm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    support_dpm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    support_wpm: list[float] = field(default_factory=lambda: [1.0, 1.0])