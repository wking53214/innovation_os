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



    def find_capability(
        self,
        capability
    ):

        return [

            agent

            for agent
            in self.agents.values()

            if capability
            in agent.capabilities

        ]
