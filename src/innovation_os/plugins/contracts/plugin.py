from dataclasses import dataclass
from typing import Protocol


class Plugin(Protocol):


    def name(self) -> str:
        ...


    def execute(
        self,
        payload: dict
    ):
        ...


@dataclass
class PluginMetadata:

    name: str

    version: str

    description: str
