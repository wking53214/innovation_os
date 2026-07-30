from dataclasses import dataclass
from typing import Optional


@dataclass
class ArchiveArtifact:
    """
    Canonical record for a file found while scanning a directory
    for archival purposes.

    This used to be defined separately in archive.connector and
    reconstruction.archive_engine, with the same core shape
    (path + artifact_type) plus one differing bonus field each
    (name vs size). Both are kept here, optional, so neither
    caller's behavior changes.
    """

    path: str
    artifact_type: str
    size: Optional[int] = None
    name: Optional[str] = None
