class FederationController:


    def __init__(
        self,
        registry
    ):

        self.registry = registry

        self.boundaries = []



    def establish_trust(
        self,
        boundary
    ):

        if boundary.approved:

            self.boundaries.append(
                boundary
            )

            return True


        return False



    def can_exchange(
        self,
        source,
        target
    ):

        for boundary in self.boundaries:

            if (
                boundary.source_tenant == source
                and
                boundary.target_tenant == target
            ):

                return True


        return False
