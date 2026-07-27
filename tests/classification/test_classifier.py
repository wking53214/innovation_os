from src.innovation_os.classification.classifier import (
    ArtifactClassifier,
)


def test_code_classification():

    classifier = ArtifactClassifier()

    result = classifier.classify(
        "class GovernanceEngine:"
    )

    assert result.artifact_type == "CODE"


def test_decision_classification():

    classifier = ArtifactClassifier()

    result = classifier.classify(
        "Decision approved human review workflow"
    )

    assert result.artifact_type == "DECISION"


def test_unknown_classification():

    classifier = ArtifactClassifier()

    result = classifier.classify(
        "random text"
    )

    assert result.artifact_type == "UNKNOWN"
