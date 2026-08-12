from innovation_os.forecast.engine import (
    ForecastEngine,
)


def test_create_scenario():

    engine = ForecastEngine()

    scenario = engine.create_scenario(
        scenario_id="SCENARIO-0001",
        solution_id="SOLUTION-0001",
        name="Positive outcome",
        outcome="Improved efficiency",
        impacts=[
            "Reduced cost",
        ],
        probability=0.75,
        risks=[
            "Adoption delay",
        ],
    )

    assert scenario.scenario_id == "SCENARIO-0001"
    assert scenario.probability == 0.75


def test_get_scenario():

    engine = ForecastEngine()

    engine.create_scenario(
        scenario_id="SCENARIO-0002",
        solution_id="SOLUTION-0002",
        name="Risk case",
        outcome="Failure",
        impacts=[],
        probability=0.25,
    )

    result = engine.get_scenario(
        "SCENARIO-0002"
    )

    assert result is not None


def test_find_by_solution():

    engine = ForecastEngine()

    engine.create_scenario(
        scenario_id="SCENARIO-0003",
        solution_id="SOLUTION-0003",
        name="Expected",
        outcome="Normal result",
        impacts=[],
        probability=0.60,
    )

    results = engine.find_by_solution(
        "SOLUTION-0003"
    )

    assert len(results) == 1
