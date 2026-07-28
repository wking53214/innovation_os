from .profile import AgentTrustProfile


class AgentTrustEvaluator:


    def __init__(self):

        self.profiles = {}


    def evaluate(
        self,
        agent,
        capability,
        score,
        governance_score
    ):

        profile = self.profiles.get(
            agent.agent_id
        )


        if profile is None:

            profile = AgentTrustProfile(
                agent_id=agent.agent_id
            )

            self.profiles[
                agent.agent_id
            ] = profile


        profile.capability_scores[
            capability
        ] = score


        profile.governance_score = (
            governance_score
        )


        profile.execution_count += 1


        return profile


    def get(
        self,
        agent_id
    ):

        return self.profiles.get(
            agent_id
        )
