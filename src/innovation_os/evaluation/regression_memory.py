class RegressionMemory:


    def __init__(self):

        self.history = []


    def record(
        self,
        result
    ):

        self.history.append(
            result
        )


    def latest(self):

        if not self.history:

            return None

        return self.history[-1]
