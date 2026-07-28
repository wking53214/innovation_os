from dataclasses import dataclass


@dataclass
class IntelligenceMemorySystem:

    index: object

    consolidator: object



    def store(
        self,
        artifact
    ):

        self.index.add(
            artifact
        )

        return artifact



    def consolidate(
        self,
        artifacts
    ):

        return self.consolidator.consolidate(
            artifacts
        )
