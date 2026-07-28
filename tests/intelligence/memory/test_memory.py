from innovation_os.intelligence.memory import (
    IntelligenceMemory,
)

from innovation_os.intelligence.contracts import (
    IntelligenceArtifact,
)


def test_memory_store():

    memory = IntelligenceMemory()

    artifact = IntelligenceArtifact(
        intelligence_type="test",
        source_system="test",
        confidence=.8,
    )

    memory.remember(
        artifact
    )

    assert memory.recall(
        artifact.artifact_id
    )
