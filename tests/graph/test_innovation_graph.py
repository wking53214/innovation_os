from src.innovation_os.graph.innovation_graph import (
    InnovationGraph,
)



def test_innovation_graph():

    graph = InnovationGraph()


    graph.add_node(
        "IDEA-SENTINEL",
        "IDEA",
    )


    graph.add_node(
        "CODE-001",
        "CODE",
    )


    graph.connect(
        "IDEA-SENTINEL",
        "CODE-001",
        "IMPLEMENTED_BY",
    )


    result = graph.related(
        "IDEA-SENTINEL"
    )


    assert "CODE-001" in result
