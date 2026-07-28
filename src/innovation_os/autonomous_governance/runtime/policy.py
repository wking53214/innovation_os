class PolicyRegistry:


    def __init__(self):

        self.policies = []



    def register(
        self,
        policy
    ):

        self.policies.append(
            policy
        )

        return policy



    def all(
        self
    ):

        return self.policies
