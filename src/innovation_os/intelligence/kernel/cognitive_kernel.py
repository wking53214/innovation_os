from dataclasses import dataclass, field
from typing import Any, Dict

from .intelligence_registry import IntelligenceRegistry


@dataclass
class CognitiveKernel:
    """
    Central coordinator for Innovation OS intelligence.

    Does not replace engines.
    Routes intelligence between components.
    """

    registry: IntelligenceRegistry = field(
        default_factory=IntelligenceRegistry
    )

    state: Dict[str, Any] = field(
        default_factory=dict
    )

    def register_engine(self, name, engine):
        self.registry.register_engine(name, engine)

    def register_adapter(self, name, adapter):
        self.registry.register_adapter(name, adapter)

    def execute(self, engine_name: str, payload):
        engine = self.registry.get_engine(engine_name)

        if engine is None:
            raise ValueError(
                f"Unknown intelligence engine: {engine_name}"
            )

        if hasattr(engine, "process"):
            return engine.process(payload)

        if callable(engine):
            return engine(payload)

        raise TypeError(
            f"Engine {engine_name} cannot execute"
        )
