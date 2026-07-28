from innovation_os.intelligence.integration import (
    IntelligenceBridge,
    IntelligenceSystemConnector,
)


def test_bridge():

    bridge = IntelligenceBridge()

    connector = IntelligenceSystemConnector(
        bridge
    )

    connector.attach(
        "memory",
        object()
    )

    assert "memory" in bridge.connected_systems()
