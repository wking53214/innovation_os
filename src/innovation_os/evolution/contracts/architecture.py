from dataclasses import dataclass, field
import uuid


@dataclass
class ArchitectureModel:

    architecture_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )

    version: str = ""

    components: list = field(
        default_factory=list
    )

    maturity: str = "planning"
