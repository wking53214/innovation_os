from dataclasses import dataclass


@dataclass
class ImportedArtifact:
    artifact_id: str
    source_path: str
    artifact_type: str
    title: str
    preview: str
