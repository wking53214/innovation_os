class AgentMemory:


    def __init__(self):

        self.storage = {}


    def remember(
        self,
        agent,
        item
    ):

        self.storage.setdefault(
            agent,
            []
        ).append(
            item
        )


    def recall(
        self,
        agent
    ):

        return self.storage.get(
            agent,
            []
        )
