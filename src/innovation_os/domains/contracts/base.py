from dataclasses import dataclass
from typing import Protocol


@dataclass
class DomainMetadata:

    name: str

    version: str

    description: str



@dataclass
class DomainSignal:

    domain: str

    category: str

    payload: dict



class DomainPack(Protocol):


    def metadata(self) -> DomainMetadata:
        ...


    def analyze(
        self,
        payload: dict
    ) -> DomainSignal:
        ...
