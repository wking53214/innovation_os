class AgentRegistry:


    def __init__(self):

        self.agents = {}


    def register(
        self,
        agent
    ):

        self.agents[
            agent.agent_id
        ] = agent


        return agent


    def get(
        self,
        agent_id
    ):

        return self.agents.get(
            agent_id
        )


    def find_by_capability(
        self,
        capability
    ):

        return [
            agent
            for agent in self.agents.values()
            if capability in agent.capabilities
        ]


    def list(
        self
    ):

        return list(
            self.agents.values()
        )
