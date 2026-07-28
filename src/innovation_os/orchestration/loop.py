class IntelligenceLoop:


    def __init__(
        self,
        controller
    ):

        self.controller = controller
        self.history = []


    def process(
        self,
        objective
    ):

        result = self.controller.run(
            objective
        )

        self.history.append(
            result
        )

        return result


    def previous(self):

        return self.history
