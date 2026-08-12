from typing import List, Optional

from innovation_os.forecast.models import (
    Scenario,
)


class ForecastEngine:

    def __init__(self):
        self.scenarios: List[Scenario] = []

    def create_scenario(
        self,
        scenario_id: str,
        solution_id: str,
        name: str,
        outcome: str,
        impacts: List[str],
        probability: float,
        risks: List[str] = None,
    ) -> Scenario:

        scenario = Scenario(
            scenario_id=scenario_id,
            solution_id=solution_id,
            name=name,
            outcome=outcome,
            impacts=impacts,
            probability=probability,
            risks=risks or [],
        )

        self.scenarios.append(scenario)

        return scenario

    def get_scenario(
        self,
        scenario_id: str,
    ) -> Optional[Scenario]:

        for scenario in self.scenarios:
            if scenario.scenario_id == scenario_id:
                return scenario

        return None

    def find_by_solution(
        self,
        solution_id: str,
    ) -> List[Scenario]:

        return [
            scenario
            for scenario in self.scenarios
            if scenario.solution_id == solution_id
        ]
