from dataclasses import dataclass, field
from typing import Any, Dict, Type


@dataclass
class IntelligenceRegistry:
    """
    Registry for intelligence engines, adapters,
    and pipeline components.
    """

    engines: Dict[str, Any] = field(default_factory=dict)
    adapters: Dict[str, Any] = field(default_factory=dict)
    contracts: Dict[str, Type] = field(default_factory=dict)

    def register_engine(self, name: str, engine: Any):
        self.engines[name] = engine

    def register_adapter(self, name: str, adapter: Any):
        self.adapters[name] = adapter

    def register_contract(self, name: str, contract: Type):
        self.contracts[name] = contract

    def get_engine(self, name: str):
        return self.engines.get(name)

    def get_adapter(self, name: str):
        return self.adapters.get(name)

    def get_contract(self, name: str):
        return self.contracts.get(name)

    def list_engines(self):
        return list(self.engines.keys())

    def list_adapters(self):
        return list(self.adapters.keys())
