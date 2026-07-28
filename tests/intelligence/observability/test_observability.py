from innovation_os.intelligence.observability import (
    IntelligenceEventBus,
    ExecutionTrace,
    MetricsCollector,
    IntelligenceMonitor,
)


def test_event_bus():

    bus = IntelligenceEventBus()

    bus.publish(
        "event"
    )

    assert bus.latest() == "event"



def test_monitor():

    trace = ExecutionTrace()

    metrics = MetricsCollector()

    monitor = IntelligenceMonitor(
        trace,
        metrics,
    )

    result = monitor.observe(
        "reasoning",
        {}
    )

    assert result["status"] == "observed"
    assert trace.count() == 1
    assert metrics.get(
        "reasoning"
    ) == 1
