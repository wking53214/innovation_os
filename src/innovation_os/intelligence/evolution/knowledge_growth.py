from dataclasses import dataclass, field
from typing import List, Any


@dataclass
class KnowledgeGrowth:
    """
    Expands intelligence knowledge state.
    """

    knowledge: List[Any] = field(
        default_factory=list
    )


    def add(self, item):

        self.knowledge.append(item)

        return item


    def size(self):

        return len(self.knowledge)
