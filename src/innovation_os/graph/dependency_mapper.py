class DependencyMapper:


    def map(
        self,
        artifacts
    ):

        graph = {}

        for artifact in artifacts:

            graph[str(artifact)] = []

        return graph
