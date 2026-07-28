class DelegationEngine:


    def select_agent(
        self,
        agents,
        capability
    ):

        for agent in agents:

            if agent.capability == capability:

                return agent

        return None


    def delegate(
        self,
        agent,
        task
    ):

        if agent is None:

            return {
                "status": "no_agent"
            }

        return agent.execute(
            task
        )
