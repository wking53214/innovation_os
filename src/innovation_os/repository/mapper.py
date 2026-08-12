from dataclasses import dataclass, field
from pathlib import Path
from typing import List



@dataclass
class RepositoryMap:

    name: str
    path: str
    files: List[str] = field(
        default_factory=list
    )
    modules: List[str] = field(
        default_factory=list
    )



class RepositoryMapper:


    def map(
        self,
        directory: str,
    ):

        root = Path(directory)


        files = [
            str(path.relative_to(root))
            for path in root.rglob("*")
            if path.is_file()
        ]


        modules = [
            file
            for file in files
            if file.endswith(".py")
        ]


        return RepositoryMap(
            name=root.name,
            path=str(root),
            files=files,
            modules=modules,
        )



    def map_repository(
        self,
        directory: str,
    ):

        """
        Legacy compatibility API.

        Returns Artifact objects
        for repository ingestion.
        """

        from innovation_os.registry.artifact_registry import (
            Artifact,
        )


        repository = self.map(
            directory
        )


        artifacts = []


        for index, file in enumerate(
            repository.files,
            start=1,
        ):

            filename = Path(file).name


            if filename.endswith(".py"):

                artifact_type = "CODE"

            elif filename.lower().endswith(
                (
                    ".md",
                    ".txt",
                    ".rst",
                    ".pdf",
                )
            ):

                artifact_type = "DOCUMENT"

            else:

                artifact_type = "RESOURCE"



            artifacts.append(
                Artifact(
                    artifact_id=f"CODE-{index:05d}",
                    artifact_type=artifact_type,
                    name=filename,
                    source=file,
                    project_id=repository.name,
                    metadata={
                        "repository": repository.name,
                    },
                )
            )


        return artifacts
