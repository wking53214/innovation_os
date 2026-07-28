from .intelligence_memory_system import IntelligenceMemorySystem
from .memory_index import MemoryIndex
from .consolidator import MemoryConsolidator


class IntelligenceMemory(IntelligenceMemorySystem):
    """
    Backwards compatible intelligence memory facade.
    """

    def __init__(
        self,
        index=None,
        consolidator=None,
    ):

        super().__init__(
            index or MemoryIndex(),
            consolidator or MemoryConsolidator(),
        )


    def remember(
        self,
        artifact
    ):

        return self.store(
            artifact
        )


    def recall(
        self,
        identifier
    ):

        return self.index.get(
            identifier
        )
