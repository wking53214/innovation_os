from innovation_os.autonomous_governance import GovernanceDecision


class GovernanceController:


    def evaluate(
        self,
        action,
        policies
    ):

        approved = len(
            policies
        ) > 0


        return GovernanceDecision(
            action=action,
            approved=approved,
            reason=(
                "policy validated"
                if approved
                else
                "no governing policy"
            ),
        )
