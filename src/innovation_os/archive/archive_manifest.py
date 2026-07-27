from dataclasses import dataclass, field
from typing import List



@dataclass
class ArchiveManifest:

    name: str
    source: str
    artifacts: List[str] = field(
        default_factory=list
    )
