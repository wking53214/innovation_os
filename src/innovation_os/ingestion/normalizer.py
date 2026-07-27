from dataclasses import dataclass



@dataclass
class NormalizedArtifact:

    name: str
    path: str
    artifact_type: str



class ArtifactNormalizer:


    def normalize(
        self,
        path,
    ):

        suffix = path.suffix.lower()


        if suffix == ".py":

            artifact_type = "CODE"

        elif suffix in [
            ".md",
            ".txt",
            ".docx",
        ]:

            artifact_type = "DOCUMENT"

        else:

            artifact_type = "UNKNOWN"


        return NormalizedArtifact(
            path.name,
            str(path),
            artifact_type,
        )
