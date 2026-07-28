class ArchitectureRegistry:


    def __init__(self):

        self.models = []



    def register(
        self,
        model
    ):

        self.models.append(
            model
        )

        return model



    def latest(
        self
    ):

        if not self.models:
            return None

        return self.models[-1]
