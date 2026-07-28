class GovernanceMeshEvaluator:


    def evaluate(
        self,
        node,
        policy
    ):


        required = policy.rules.get(
            "required_capabilities",
            []
        )


        compliant = all(

            capability
            in node.capabilities

            for capability
            in required

        )


        return {

            "node_id":
            node.node_id,

            "policy":
            policy.name,

            "compliant":
            compliant

        }
