from innovation_os.intelligence.reasoning import (
    ReasoningChain,
    CausalEngine,
    ExplanationGraph,
)


def test_reasoning():

    chain = ReasoningChain()

    chain.add("observe")
    chain.add("infer")

    assert chain.execute() == ["observe", "infer"]


def test_causal():

    engine = CausalEngine()

    engine.connect(
        "signal",
        "decision"
    )

    assert engine.causes("decision") == ["signal"]
    assert engine.causes("unrelated") == []


def test_explanation():

    graph = ExplanationGraph()

    graph.add_node(
        "A"
    )

    graph.add_node(
        "B"
    )

    graph.connect(
        "A",
        "B"
    )

    assert graph.nodes == {"A": {}, "B": {}}
    assert graph.edges == [("A", "B")]
