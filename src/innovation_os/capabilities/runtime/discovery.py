class CapabilityDiscovery:


    def __init__(
        self,
        catalog
    ):

        self.catalog = catalog



    def find(
        self,
        category
    ):

        return self.catalog.search(
            category
        )
