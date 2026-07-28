class FederationController:


    def __init__(
        self,
        trust_store
    ):

        self.trust_store = trust_store



    def approve(
        self,
        node_id
    ):

        record = self.trust_store.get(
            node_id
        )


        if record is None:

            return False


        return record.verified
