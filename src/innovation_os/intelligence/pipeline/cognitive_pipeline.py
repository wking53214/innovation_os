from dataclasses import dataclass, field
from typing import Any

from .intelligence_pipeline import IntelligencePipeline


@dataclass
class CognitivePipeline:
    """
    Higher-level cognitive execution pipeline.

    Connects intelligence stages without coupling
    individual engines.
    """

    pipeline: IntelligencePipeline = field(
        default_factory=IntelligencePipeline
    )

    def register(self, stage):
        self.pipeline.add_stage(stage)

    def process(self, input_data: Any):

        return self.pipeline.execute(
            input_data
        )
