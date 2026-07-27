from src.innovation_os.knowledge_graph.engine import (
    KnowledgeGraphEngine,
)


def test_relationship_creation():

    graph = KnowledgeGraphEngine()

    edge = graph.connect(
        "PROJECT-001",
        "implemented_by",
        "CODE-001",
    )


    assert edge.source == "PROJECT-001"
    assert edge.relationship == "implemented_by"
    assert edge.target == "CODE-001"



def test_find_connections():

    graph = KnowledgeGraphEngine()

    graph.connect(
        "IDEA-001",
        "originated_from",
        "CHAT-001",
    )


    results = graph.find_connections(
        "IDEA-001"
    )


    assert len(results) == 1
    assert results[0].target == "CHAT-001"



def test_relationship_filter():

    graph = KnowledgeGraphEngine()

    graph.connect(
        "PROJECT-001",
        "implemented_by",
        "CODE-001",
    )

    graph.connect(
        "PROJECT-001",
        "validated_by",
        "DECISION-001",
    )


    results = graph.find_by_type(
        "validated_by"
    )


    assert len(results) == 1
