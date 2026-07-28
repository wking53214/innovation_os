class FederatedKnowledgeStore:


    def __init__(self):

        self.artifacts = {}



    def publish(
        self,
        artifact
    ):

        self.artifacts[
            artifact.artifact_id
        ] = artifact


        return artifact



    def retrieve(
        self,
        artifact_id
    ):

        return self.artifacts.get(
            artifact_id
        )



    def query(
        self,
        knowledge_type
    ):

        return [

            artifact

            for artifact
            in self.artifacts.values()

            if artifact.knowledge_type
            ==
            knowledge_type

        ]
