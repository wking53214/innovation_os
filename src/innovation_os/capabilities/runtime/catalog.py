class CapabilityCatalog:


    def __init__(self):

        self.capabilities = {}



    def register(
        self,
        capability
    ):

        self.capabilities[
            capability.capability_id
        ] = capability


        return capability



    def get(
        self,
        capability_id
    ):

        return self.capabilities.get(
            capability_id
        )



    def search(
        self,
        category=None
    ):

        results = list(
            self.capabilities.values()
        )


        if category:

            results = [
                item
                for item in results
                if item.category == category
            ]


        return results
