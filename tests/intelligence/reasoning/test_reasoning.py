from innovation_os.intelligence.reasoning import (
    ReasoningChain,
    CausalEngine,
    ExplanationGraph,
)


def test_reasoning():

    chain = ReasoningChain()

    chain.add("observe")

    assert chain.execute()


def test_causal():

    engine = CausalEngine()

    engine.connect(
        "signal",
        "decision"
    )

    assert engine.causes(
        "decision"
    )


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

    assert graph.edges
