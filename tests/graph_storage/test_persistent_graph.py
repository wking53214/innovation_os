from innovation_os.graph_storage.persistent_graph import (
    PersistentInnovationGraph,
)


def test_graph_node_persistence():

    graph = PersistentInnovationGraph(
        ":memory:"
    )

    graph.add_node(
        "IDEA-001",
        "IDEA",
        "Governed AI",
    )

    node = graph.get_node(
        "IDEA-001"
    )

    assert node[0] == "IDEA-001"
    assert node[2] == "Governed AI"


def test_graph_relationship_persistence():

    graph = PersistentInnovationGraph(
        ":memory:"
    )

    graph.add_relationship(
        "CODE-001",
        "IDEA-001",
        "SUPPORTS",
    )

    links = graph.get_connections(
        "CODE-001"
    )

    assert len(links) == 1
    assert links[0][3] == "SUPPORTS"
