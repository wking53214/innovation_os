class MemoryConsolidator:


    def consolidate(
        self,
        artifacts
    ):

        merged = {}

        for artifact in artifacts:

            merged.update(
                artifact.content
            )

        return merged
