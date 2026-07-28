from innovation_os.intelligence.contracts import IntelligenceArtifact


def test_intelligence_artifact_validation():

    artifact = IntelligenceArtifact(
        intelligence_type="pattern",
        source_system="pattern_engine",
        confidence=0.85,
    )

    assert artifact.validate()


def test_invalid_confidence():

    artifact = IntelligenceArtifact(
        intelligence_type="pattern",
        source_system="pattern_engine",
        confidence=2.0,
    )

    assert not artifact.validate()
