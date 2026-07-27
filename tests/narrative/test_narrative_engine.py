from src.innovation_os.narrative.engine import (
    ExecutiveNarrativeEngine,
)



def test_narrative_generation():

    engine = ExecutiveNarrativeEngine()


    result = engine.generate(
        "Sentinel OS",
        "an AI governance platform",
        [
            "GSA",
            "Audit Ledger",
        ],
    )


    assert result.title == "Sentinel OS"
    assert len(result.artifacts) == 2
    assert "AI governance" in result.summary
