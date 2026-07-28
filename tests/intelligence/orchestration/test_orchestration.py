from innovation_os.intelligence.orchestration import (
    IntelligenceOrchestrator,
    TaskPlanner,
    PriorityEngine,
    ExecutionGraph,
)


def test_orchestration():

    orchestrator = IntelligenceOrchestrator(
        TaskPlanner(),
        PriorityEngine(),
        ExecutionGraph(),
    )

    result = orchestrator.execute(
        "analyze repository"
    )

    assert result[0]["priority"] == 1
    assert len(
        orchestrator.graph.nodes
    ) == 1
