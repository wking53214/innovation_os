from innovation_os.decision.engine import DecisionEngine


def test_create_decision():
    engine = DecisionEngine()

    decision = engine.create_decision(
        decision_id="DECISION-0001",
        problem_id="PROBLEM-0001",
        context="Selecting architecture direction",
        options=[
            "Option A",
            "Option B",
            "Option C",
        ],
        selected_option="Option B",
        rejected_options=[
            "Option A",
            "Option C",
        ],
        assumptions=[
            "Scalability is required",
            "Human approval is required",
        ],
        confidence=0.85,
        approval="Owner approved",
    )

    assert decision.decision_id == "DECISION-0001"
    assert decision.selected_option == "Option B"
    assert decision.confidence == 0.85


def test_retrieve_decision():
    engine = DecisionEngine()

    engine.create_decision(
        decision_id="DECISION-0001",
        problem_id="PROBLEM-0001",
        context="Testing retrieval",
        options=["A", "B"],
        selected_option="B",
        rejected_options=["A"],
        assumptions=["Test assumption"],
        confidence=0.90,
        approval="Owner approved",
    )

    decision = engine.get_decision("DECISION-0001")

    assert decision is not None
    assert decision.problem_id == "PROBLEM-0001"


def test_get_decisions_for_problem():
    engine = DecisionEngine()

    engine.create_decision(
        decision_id="DECISION-0001",
        problem_id="PROBLEM-0001",
        context="Problem decision",
        options=["A", "B"],
        selected_option="A",
        rejected_options=["B"],
        assumptions=[],
        confidence=0.75,
        approval="Owner approved",
    )

    decisions = engine.get_decisions_for_problem(
        "PROBLEM-0001"
    )

    assert len(decisions) == 1
