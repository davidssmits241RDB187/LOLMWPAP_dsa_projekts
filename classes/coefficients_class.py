from dataclasses import dataclass, field

@dataclass
class Coefficients:
    
    gold_per_minute_or_gold_lead: list[float] = field(default_factory=lambda: [1.0, 1.0])
    kills_per_game: list[float] = field(default_factory=lambda: [1.0, 1.0])
    avg_tower_difference: list[float] = field(default_factory=lambda: [1.0, 1.0])
    dragons_per_game: list[float] = field(default_factory=lambda: [1.0, 1.0])
    nashor_per_game: list[float] = field(default_factory=lambda: [1.0, 1.0])
    
    top_kda: list[float] = field(default_factory=lambda: [1.0, 1.0])
    top_csm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    top_dmg: list[float] = field(default_factory=lambda: [1.0, 1.0])
    top_vspm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    
    mid_kda: list[float] = field(default_factory=lambda: [1.0, 1.0])
    mid_csm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    mid_dmg: list[float] = field(default_factory=lambda: [1.0, 1.0])
    mid_vspm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    
    jungle_kda: list[float] = field(default_factory=lambda: [1.0, 1.0])
    jungle_csm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    jungle_dmg: list[float] = field(default_factory=lambda: [1.0, 1.0])
    jungle_vspm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    
    bot_kda: list[float] = field(default_factory=lambda: [1.0, 1.0])
    bot_csm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    bot_dmg: list[float] = field(default_factory=lambda: [1.0, 1.0])
    bot_vspm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    
    support_kda: list[float] = field(default_factory=lambda: [1.0, 1.0])
    support_csm: list[float] = field(default_factory=lambda: [1.0, 1.0])
    support_dmg: list[float] = field(default_factory=lambda: [1.0, 1.0])
    support_vspm: list[float] = field(default_factory=lambda: [1.0, 1.0])