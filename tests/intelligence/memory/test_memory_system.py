from innovation_os.intelligence.memory import (
    MemoryArtifact,
    MemoryIndex,
    RetrievalEngine,
    MemoryConsolidator,
    IntelligenceMemorySystem,
)



def test_memory_storage():

    system = IntelligenceMemorySystem(
        MemoryIndex(),
        MemoryConsolidator(),
    )

    artifact = MemoryArtifact(
        "one",
        {
            "idea": "AI system"
        }
    )

    system.store(
        artifact
    )

    assert system.index.size() == 1



def test_memory_retrieval():

    index = MemoryIndex()

    artifact = MemoryArtifact(
        "a",
        {
            "value": 10
        }
    )

    index.add(
        artifact
    )

    retrieval = RetrievalEngine(
        index
    )

    result = retrieval.retrieve(
        "a"
    )

    assert result.content["value"] == 10



def test_consolidation():

    engine = MemoryConsolidator()

    result = engine.consolidate(
        [
            MemoryArtifact(
                "1",
                {"a":1}
            ),
            MemoryArtifact(
                "2",
                {"b":2}
            ),
        ]
    )

    assert result == {
        "a":1,
        "b":2
    }
