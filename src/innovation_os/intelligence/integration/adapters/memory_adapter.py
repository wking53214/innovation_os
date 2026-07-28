from dataclasses import dataclass


@dataclass
class IntelligenceMemoryAdapter:
    """
    Intelligence access boundary for memory subsystem.
    """

    memory=None


    def store(
        self,
        artifact
    ):

        if self.memory and hasattr(
            self.memory,
            "store"
        ):
            return self.memory.store(
                artifact
            )

        return artifact


    def retrieve(
        self,
        key
    ):

        if self.memory and hasattr(
            self.memory,
            "retrieve"
        ):
            return self.memory.retrieve(
                key
            )

        return None
