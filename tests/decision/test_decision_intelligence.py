from src.innovation_os.decision.intelligence import (
    DecisionIntelligenceEngine,
)



def test_decision_recording():

    engine = DecisionIntelligenceEngine()


    result = engine.record(
        "DECISION-001",
        "PostgreSQL",
        "Need transactional integrity",
        [
            "SQLite",
            "MongoDB",
        ],
        "Production ledger enabled",
    )


    assert result.choice == "PostgreSQL"
    assert len(result.alternatives) == 2


    found = engine.search(
        "transactional"
    )


    assert len(found) == 1
