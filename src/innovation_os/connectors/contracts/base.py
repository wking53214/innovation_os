from dataclasses import dataclass
from typing import Protocol


@dataclass
class ConnectorMetadata:

    name: str

    version: str

    source_type: str



@dataclass
class ConnectorEvent:

    connector: str

    event_type: str

    payload: dict



class Connector(Protocol):


    def connect(self):
        ...


    def collect(self):
        ...
