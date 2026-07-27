from dataclasses import dataclass
from typing import List


@dataclass
class ReconstructedProject:

    project_id: str
    name: str
    artifacts: List[str]
    concepts: List[str]
    confidence: float



class ProjectReconstructionEngine:


    def reconstruct(
        self,
        project_id: str,
        artifacts: List[str],
        concepts: List[str],
    ):

        confidence = 0.0


        if artifacts:

            confidence += 50


        if concepts:

            confidence += 50


        return ReconstructedProject(
            project_id,
            project_id.replace(
                "-",
                " ",
            ),
            artifacts,
            concepts,
            confidence,
        )
