from innovation_os.intelligence.health import (
    IntelligenceHealthMonitor,
)


def test_health():

    monitor = IntelligenceHealthMonitor()

    monitor.register(
        "runtime",
        True
    )

    assert monitor.healthy()
