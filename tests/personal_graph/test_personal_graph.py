from src.innovation_os.personal_graph.engine import (
    PersonalInnovationGraph,
)


def test_graph_nodes():

    graph = PersonalInnovationGraph()


    graph.add_node(
        "PROJECT-001",
        "PROJECT",
        "Sentinel OS",
    )


    graph.add_node(
        "CODE-001",
        "CODE",
        "Governance Engine",
    )


    assert len(graph.nodes) == 2



def test_graph_relationships():

    graph = PersonalInnovationGraph()


    graph.add_node(
        "PROJECT-001",
        "PROJECT",
        "Sentinel OS",
    )


    graph.add_node(
        "CODE-001",
        "CODE",
        "Engine",
    )


    graph.connect(
        "PROJECT-001",
        "implemented_by",
        "CODE-001",
    )


    links = graph.neighbors(
        "PROJECT-001"
    )


    assert "CODE-001" in links



def test_type_search():

    graph = PersonalInnovationGraph()


    graph.add_node(
        "IDEA-001",
        "IDEA",
        "AI Governance",
    )


    results = graph.find_by_type(
        "IDEA"
    )


    assert len(results) == 1
