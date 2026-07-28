from abc import ABC, abstractmethod


class IntelligenceAdapter(ABC):
    """
    Adapter boundary between existing engines
    and the intelligence layer.
    """

    name: str = "base"

    @abstractmethod
    def translate(self, data):
        pass

    def process(self, data):
        return self.translate(data)
