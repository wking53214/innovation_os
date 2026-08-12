from innovation_os.reasoning.engine import (
    ReasoningEngine,
)


def test_reasoning_analysis():

    engine = ReasoningEngine()


    engine.add_context(
        "Sentinel OS",
        [
            "Governance Engine",
            "Decision Ledger",
            "Audit Pipeline",
        ],
    )


    insight = engine.analyze(
        "Sentinel OS"
    )


    assert insight.subject == "Sentinel OS"
    assert len(
        insight.supporting_artifacts
    ) == 3


def test_unknown_subject():

    engine = ReasoningEngine()


    result = engine.analyze(
        "Unknown Project"
    )


    assert (
        result.summary
        ==
        "No innovation context found."
    )
