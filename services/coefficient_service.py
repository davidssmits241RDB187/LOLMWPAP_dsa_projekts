from services.team_service import Team
from data.data_types import CoefficientValues, CoefficientCoeffs, CoefficientRoles, CoefficientPlayerAttributes, CoefficientPlayerCoeffs

from dataclasses import dataclass, field

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

    def evaluate_coefficients(self, winning_team: Team, losing_team: Team):
        for i in range(5):
            win_value = float(getattr(winning_team, CoefficientValues[i]))
            loss_value = float(getattr(losing_team, CoefficientValues[i]))
            coeff_value = getattr(self, CoefficientCoeffs[i])
            if win_value > loss_value:
                coeff_value[0] += 1.0
            elif win_value < loss_value:
                coeff_value[1] += 1.0
            setattr(self, CoefficientCoeffs[i], coeff_value)
                
        for i in range(5):
            winning_player = getattr(winning_team, CoefficientRoles[i])
            losing_player = getattr(losing_team, CoefficientRoles[i])
            for j in range(3):
                win_value = float(winning_player[CoefficientPlayerAttributes[j]])
                loss_value = float(losing_player[CoefficientPlayerAttributes[j]])
                coeff = CoefficientRoles[j] + "_" + CoefficientPlayerCoeffs[j]
                coeff_value = getattr(self, coeff)
                if win_value > loss_value:
                    coeff_value[0] += 1.0
                elif win_value < loss_value:
                    coeff_value[1] += 1.0
                setattr(self, coeff, coeff_value)
