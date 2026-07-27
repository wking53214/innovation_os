from dataclasses import dataclass


@dataclass
class ClassificationResult:

    artifact: str
    artifact_type: str
    confidence: float



class ArtifactClassifier:


    def classify(
        self,
        artifact: str,
    ):

        text = artifact.lower()


        if (
            "class "
            in text
            or "def "
            in text
            or "import "
            in text
        ):

            return ClassificationResult(
                artifact,
                "CODE",
                95.0,
            )


        if (
            "decision"
            in text
            or "decided"
            in text
            or "approved"
            in text
        ):

            return ClassificationResult(
                artifact,
                "DECISION",
                85.0,
            )


        if (
            "architecture"
            in text
            or "system design"
            in text
            or "framework"
            in text
        ):

            return ClassificationResult(
                artifact,
                "ARCHITECTURE",
                80.0,
            )


        if (
            "idea"
            in text
            or "should create"
            in text
            or "concept"
            in text
        ):

            return ClassificationResult(
                artifact,
                "IDEA",
                75.0,
            )


        if (
            "research"
            in text
            or "study"
            in text
            or "analysis"
            in text
        ):

            return ClassificationResult(
                artifact,
                "RESEARCH",
                70.0,
            )


        return ClassificationResult(
            artifact,
            "UNKNOWN",
            0.0,
        )
