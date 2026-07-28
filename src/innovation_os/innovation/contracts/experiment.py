from dataclasses import dataclass, field
import uuid


@dataclass
class InnovationExperiment:

    experiment_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )

    hypothesis_id: str = ""

    objective: str = ""

    result: str = "pending"

    score: float = 0.0
