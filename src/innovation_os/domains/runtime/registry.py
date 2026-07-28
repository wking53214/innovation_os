class DomainRegistry:


    def __init__(self):

        self.domains = {}


    def register(
        self,
        domain
    ):

        metadata = domain.metadata()

        self.domains[
            metadata.name
        ] = domain

        return metadata


    def get(
        self,
        name
    ):

        return self.domains.get(
            name
        )


    def list(
        self
    ):

        return [
            domain.metadata()
            for domain in self.domains.values()
        ]
