class AgentSelector:


    def __init__(self):

        self.agents = {}


    def register(
        self,
        name,
        agent
    ):

        self.agents[name] = agent


    def select(
        self,
        capability
    ):

        return self.agents.get(
            capability
        )
