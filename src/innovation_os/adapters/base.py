from abc import ABC, abstractmethod


class IntelligenceAdapter(ABC):

    @abstractmethod
    def name(self):
        pass


    @abstractmethod
    def execute(
        self,
        payload
    ):
        pass
