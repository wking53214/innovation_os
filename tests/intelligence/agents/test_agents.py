from innovation_os.intelligence.agents import (
    CapabilityRegistry,
    TaskRouter,
    IntelligenceAgent,
)


def test_capability_registry():

    registry = CapabilityRegistry()

    registry.register(
        "echo",
        lambda x: x
    )

    assert registry.get(
        "echo"
    )


def test_agent_execution():

    registry = CapabilityRegistry()

    registry.register(
        "echo",
        lambda x: x
    )

    router = TaskRouter(
        registry
    )

    agent = IntelligenceAgent(
        "test_agent",
        router
    )

    result = agent.execute(
        "echo",
        {
            "value": 1
        }
    )

    assert result["value"] == 1
