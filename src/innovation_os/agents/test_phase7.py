from innovation_os.agents.runtime import MultiAgentRuntime
from innovation_os.agents import Agent


runtime = MultiAgentRuntime()


runtime.add_agent(
    Agent(
        name="researcher",
        capability="research"
    )
)


result = runtime.solve(
    "research",
    "Analyze repository"
)


assert result["status"] == "synthesized"

print(
    "PHASE 7 MULTI AGENT ONLINE"
)
