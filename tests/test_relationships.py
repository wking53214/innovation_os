from innovation_os.relationships import RelationshipEngine


def test_create_relationship():
    engine = RelationshipEngine()

    relationship = engine.connect(
        source_id="PROB-0001",
        target_id="CON-0001",
        relationship_type="created",
    )

    assert relationship.source_id == "PROB-0001"
    assert relationship.target_id == "CON-0001"
    assert relationship.relationship_type == "created"


def test_find_connections():
    engine = RelationshipEngine()

    engine.connect(
        source_id="PROB-0001",
        target_id="CON-0001",
        relationship_type="created",
    )

    connections = engine.find_connections("PROB-0001")

    assert len(connections) == 1
    assert connections[0].target_id == "CON-0001"