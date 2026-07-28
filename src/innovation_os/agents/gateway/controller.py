from .decision import AgentExecutionDecision


class AgentGovernanceGateway:


    def __init__(
        self,
        registry,
        evaluator,
        policy
    ):

        self.registry = registry

        self.evaluator = evaluator

        self.policy = policy



    def authorize(
        self,
        request
    ):

        agent = self.registry.get(
            request.agent_id
        )


        if agent is None:

            return AgentExecutionDecision(
                False,
                "agent_not_found",
                request.agent_id,
                request.capability,
            )


        if request.capability not in agent.capabilities:

            return AgentExecutionDecision(
                False,
                "capability_not_registered",
                request.agent_id,
                request.capability,
            )


        profile = self.evaluator.get(
            agent.agent_id
        )


        if not self.policy.allowed(
            profile
        ):

            return AgentExecutionDecision(
                False,
                "trust_threshold_failed",
                request.agent_id,
                request.capability,
            )


        return AgentExecutionDecision(
            True,
            "approved",
            request.agent_id,
            request.capability,
        )
