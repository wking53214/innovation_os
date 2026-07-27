from src.innovation_os.relationships.relationship_engine import (
    RelationshipEngine,
)



def test_relationship_creation():

    engine = RelationshipEngine()


    engine.connect(
        "IDEA-001",
        "CODE-001",
        "IMPLEMENTED_BY",
    )


    engine.connect(
        "IDEA-001",
        "PROJECT-SENTINEL",
        "BECAME_PROJECT",
    )


    result = engine.find_links(
        "IDEA-001"
    )


    assert len(result) == 2

    assert result[0].relationship_type == "IMPLEMENTED_BY"
