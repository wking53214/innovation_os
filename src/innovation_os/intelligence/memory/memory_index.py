class MemoryIndex:


    def __init__(self):

        self.index = {}



    def add(
        self,
        artifact
    ):

        self.index[
            artifact.identifier
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
