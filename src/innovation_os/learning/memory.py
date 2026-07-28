class LearningMemory:


    def __init__(self):

        self.patterns = {}


    def reinforce(
        self,
        key,
        value
    ):

        self.patterns[key] = (
            self.patterns.get(
                key,
                0
            ) + value
        )


    def recall(
        self,
        key
    ):

        return self.patterns.get(
            key,
            0
        )
