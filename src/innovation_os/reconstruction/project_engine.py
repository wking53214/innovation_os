from dataclasses import dataclass, field
from typing import List


@dataclass
class ProjectCandidate:

    project_id: str
    name: str
    evidence: List[str] = field(default_factory=list)
    confidence: float = 0.0


class ProjectReconstructionEngine:


    def __init__(self):

        self.projects = []


    def reconstruct(
        self,
        name: str,
        artifacts: List[str],
    ):

        evidence = []

        keywords = [
            "code",
            "conversation",
            "decision",
            "document",
            "idea",
        ]


        for artifact in artifacts:

            lower = artifact.lower()

            if any(
                keyword in lower
                for keyword in keywords
            ):
                evidence.append(
                    artifact
                )


        confidence = 0

        if evidence:
            confidence = min(
                len(evidence) * 20,
                100,
            )


        project = ProjectCandidate(
            project_id=f"PROJECT-{len(self.projects)+1:04d}",
            name=name,
            evidence=evidence,
            confidence=confidence,
        )


        self.projects.append(
            project
        )

        return project
