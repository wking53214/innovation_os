class KnowledgeExchangeService:


    def __init__(
        self,
        store
    ):

        self.store = store



    def exchange(
        self,
        artifact
    ):

        return self.store.publish(
            artifact
        )



    def discover(
        self,
        knowledge_type
    ):

        return self.store.query(
            knowledge_type
        )
