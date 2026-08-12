from innovation_os.graph.models import (
    InnovationGraph,
)


def test_graph_nodes():

    graph = InnovationGraph()

    node = graph.add_node(
        node_id="IDEA-001",
        node_type="IDEA",
        label="Governed AI",
    )

    assert node.label == "Governed AI"


def test_graph_relationship():

    graph = InnovationGraph()

    graph.add_node(
        "PROBLEM-001",
        "PROBLEM",
        "AI Governance",
    )

    graph.add_node(
        "IDEA-001",
        "IDEA",
        "Governance Platform",
    )

    relationship = graph.connect(
        "PROBLEM-001",
        "IDEA-001",
        "GENERATES",
    )

    assert relationship.relationship == "GENERATES"

    connections = graph.get_connections(
        "PROBLEM-001"
    )

    assert len(connections) == 1
