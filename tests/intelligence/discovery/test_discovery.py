from innovation_os.intelligence.discovery import (
    DiscoveryEngine,
    RelationshipDiscovery,
    AnomalyDetector,
)


def test_discovery():

    engine = DiscoveryEngine()

    result = engine.discover(
        {"signal": "test"}
    )

    assert result["type"] == "discovery"


def test_relationships():

    engine = RelationshipDiscovery()

    result = engine.discover(
        "A",
        "B"
    )

    assert result["type"] == "related"


def test_anomaly():

    detector = AnomalyDetector()

    result = detector.detect(
        10,
        expected=5
    )

    assert result
