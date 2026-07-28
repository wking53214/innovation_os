class RetrievalEngine:


    def __init__(
        self,
        memory_index
    ):

        self.memory_index = memory_index



    def retrieve(
        self,
        identifier
    ):

        return self.memory_index.get(
            identifier
        )
