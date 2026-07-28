class MemoryIndex:
    """
    Storage index supporting IntelligenceArtifact contracts.
    """


    def __init__(self):

        self.index = {}



    def _key(
        self,
        artifact
    ):

        if hasattr(
            artifact,
            "identifier"
        ):
            return artifact.identifier

        if hasattr(
            artifact,
            "artifact_id"
        ):
            return artifact.artifact_id

        raise AttributeError(
            "Artifact requires identifier or artifact_id"
        )



    def add(
        self,
        artifact
    ):

        self.index[
            self._key(artifact)
        ] = artifact



    def get(
        self,
        identifier
    ):

        return self.index.get(
            identifier
        )



    def size(self):

        return len(
            self.index
        )
