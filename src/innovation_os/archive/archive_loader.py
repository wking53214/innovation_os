from pathlib import Path

from .archive_manifest import ArchiveManifest



class ArchiveLoader:


    def load(
        self,
        directory: str,
    ):

        root = Path(directory)


        artifacts = [
            str(path)
            for path in root.rglob("*")
            if path.is_file()
        ]


        return ArchiveManifest(
            name=root.name,
            source=str(root),
            artifacts=artifacts,
        )
