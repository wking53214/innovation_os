class DomainRuntime:


    def __init__(
        self,
        registry
    ):

        self.registry = registry


    def execute(
        self,
        domain_name,
        payload
    ):

        domain = self.registry.get(
            domain_name
        )

        if domain is None:

            return None


        return domain.analyze(
            payload
        )
