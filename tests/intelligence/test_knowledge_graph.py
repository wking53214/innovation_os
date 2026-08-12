from innovation_os.intelligence.knowledge_graph import (
    KnowledgeGraph,
)



def test_graph_relationship_path():

    graph = KnowledgeGraph()


    graph.add_node(
        "PROJECT-001",
        "PROJECT",
        "Sentinel OS",
    )


    graph.add_node(
        "CODE-001",
        "CODE",
        "gsa_gateway.py",
    )


    graph.add_node(
        "CONCEPT-001",
        "CONCEPT",
        "AI Governance",
    )


    graph.connect(
        "PROJECT-001",
        "CODE-001",
        "contains",
    )


    graph.connect(
        "CODE-001",
        "CONCEPT-001",
        "implements",
    )


    path = graph.related_path(
        "PROJECT-001",
        "CONCEPT-001",
    )


    assert path == [
        "PROJECT-001",
        "CODE-001",
        "CONCEPT-001",
    ]
