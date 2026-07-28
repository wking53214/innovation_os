class EnvironmentManager:


    def __init__(self):

        self.environments = {}



    def create(
        self,
        environment
    ):

        self.environments[
            environment.name
        ] = environment


        return environment



    def get(
        self,
        name
    ):

        return self.environments.get(
            name
        )
