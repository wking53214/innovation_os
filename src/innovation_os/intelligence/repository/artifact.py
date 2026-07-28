from dataclasses import dataclass, field


@dataclass
class RepositoryArtifact:

    name: str
    artifact_type: str
    metadata: dict = field(
        default_factory=dict
    )
