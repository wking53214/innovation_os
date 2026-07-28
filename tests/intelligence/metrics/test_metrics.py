from innovation_os.intelligence.metrics import (
    IntelligenceMetrics,
)


def test_metrics():

    metrics = IntelligenceMetrics()

    metrics.increment(
        "executions"
    )

    metrics.record(
        "confidence",
        .9
    )

    assert metrics.get(
        "executions"
    ) == 1

    assert metrics.get(
        "confidence"
    ) == .9
