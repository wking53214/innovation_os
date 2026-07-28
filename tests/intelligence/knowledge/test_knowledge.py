from innovation_os.intelligence.knowledge import (
    KnowledgeEntity,
    KnowledgeRelationship,
    EntityResolver,
    KnowledgeInference,
    KnowledgeFabric,
)


def test_entity_creation():

    entity = KnowledgeEntity(
        "Innovation",
        "concept",
    )

    assert entity.name == "Innovation"



def test_entity_resolution():

    resolver = EntityResolver()

    a = KnowledgeEntity(
        "AI"
        ,
        "technology"
    )

    b = KnowledgeEntity(
        "ai",
        "technology"
    )

    assert resolver.match(
        a,
        b
    )



def test_knowledge_fabric():

    fabric = KnowledgeFabric()

    entity = KnowledgeEntity(
        "System",
        "architecture"
    )

    fabric.add_entity(
        entity
    )

    assert fabric.entity_count() == 1



def test_relationship_inference():

    inference = KnowledgeInference()

    relationship = KnowledgeRelationship(
        "a",
        "b",
        "depends_on",
    )

    result = inference.infer(
        relationship
    )

    assert result.relation_type == "depends_on"
