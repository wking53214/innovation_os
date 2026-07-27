from dataclasses import dataclass
from typing import List


@dataclass
class HealthIssue:

    artifact_id: str
    issue_type: str
    severity: str
    description: str



class InnovationHealthMonitor:


    def analyze(
        self,
        artifacts: List[dict],
    ):

        issues = []


        for artifact in artifacts:

            artifact_id = artifact.get(
                "id"
            )

            artifact_type = artifact.get(
                "type"
            )


            if (
                artifact_type == "IDEA"
                and not artifact.get("project")
            ):

                issues.append(
                    HealthIssue(
                        artifact_id,
                        "ORPHAN_IDEA",
                        "MEDIUM",
                        "Idea has no linked project",
                    )
                )


            if (
                artifact_type == "CODE"
                and not artifact.get("project")
            ):

                issues.append(
                    HealthIssue(
                        artifact_id,
                        "UNLINKED_CODE",
                        "HIGH",
                        "Code has no parent project",
                    )
                )


            if (
                artifact_type == "PROJECT"
                and not artifact.get("decision")
            ):

                issues.append(
                    HealthIssue(
                        artifact_id,
                        "MISSING_DECISION",
                        "LOW",
                        "Project has no decision record",
                    )
                )


        return issues
