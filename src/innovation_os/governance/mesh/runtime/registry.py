class PolicyMeshRegistry:


    def __init__(self):

        self.policies = {}



    def publish(
        self,
        policy
    ):

        self.policies[
            policy.policy_id
        ] = policy


        return policy



    def get(
        self,
        policy_id
    ):

        return self.policies.get(
            policy_id
        )



    def all(
        self
    ):

        return list(
            self.policies.values()
        )
