from services.team_service import Team
from data.data_types import CoefficientValues, CoefficientRoles, CoefficientPlayerAttributes

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

    def evaluate_coefficients(self, winning_team: Team, losing_team: Team):
        for i in range(5):
            win_value = getattr(winning_team, CoefficientValues[i])
            loss_value = getattr(losing_team, CoefficientValues[i])
            coeff_value = getattr(self, CoefficientValues[i])
            if win_value > loss_value:
                coeff_value[0] += 1.0
            elif win_value < loss_value:
                coeff_value[1] += 1.0
            setattr(self, CoefficientValues[i], coeff_value)
                
        for i in range(5):
            winning_player = getattr(winning_team, CoefficientRoles[i])
            losing_player = getattr(losing_team, CoefficientRoles[i])
            for j in range(4):
                win_value = getattr(winning_player, CoefficientPlayerAttributes[j])
                loss_value = getattr(losing_player, CoefficientPlayerAttributes[j])
                coeff = CoefficientRoles[i] + "_" + CoefficientPlayerAttributes[j]
                coeff_value = getattr(self, coeff)
                if win_value > loss_value:
                    coeff_value[0] += 1.0
                elif win_value < loss_value:
                    coeff_value[1] += 1.0
                setattr(self, coeff, coeff_value)
