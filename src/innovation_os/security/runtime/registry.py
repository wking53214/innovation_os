class IdentityRegistry:


    def __init__(self):

        self.identities = {}



    def register(
        self,
        identity
    ):

        self.identities[
            identity.name
        ] = identity


        return identity



    def get(
        self,
        name
    ):

        return self.identities.get(
            name
        )
