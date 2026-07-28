class IntelligenceMetrics:


    def __init__(self):

        self.values = {}



    def increment(
        self,
        name,
        value=1
    ):

        self.values[name] = (
            self.values.get(
                name,
                0
            )
            +
            value
        )



    def get(
        self,
        name
    ):

        return self.values.get(
            name,
            0
        )
