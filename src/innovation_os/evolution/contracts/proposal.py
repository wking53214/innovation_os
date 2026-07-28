from dataclasses import dataclass, field
import uuid


@dataclass
class EvolutionProposal:

    proposal_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )

    title: str = ""

    target_version: str = ""

    capabilities: list = field(
        default_factory=list
    )

    approved: bool = False
