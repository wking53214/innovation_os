from .core.agent import Agent
from .core.registry import AgentRegistry
from .coordination.delegator import DelegationEngine
from .coordination.collaboration import CollaborationEngine


class MultiAgentRuntime:


    def __init__(self):

        self.registry = AgentRegistry()

        self.delegator = DelegationEngine()

        self.collaboration = CollaborationEngine()



    def add_agent(
        self,
        agent
    ):

        self.registry.register(
            agent
        )


    def solve(
        self,
        capability,
        task
    ):

        agent = self.delegator.select_agent(
            self.registry.all(),
            capability
        )

        result = self.delegator.delegate(
            agent,
            task
        )

        return self.collaboration.combine(
            [result]
        )
