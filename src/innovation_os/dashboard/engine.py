from dataclasses import dataclass
from typing import Dict, List


@dataclass
class DashboardReport:

    total_artifacts: int
    active_projects: int
    health_issues: int
    recommendations: List[str]



class InnovationDashboard:


    def generate(
        self,
        artifacts: List[dict],
        issues: List,
        recommendations: List[str],
    ):

        projects = [
            artifact
            for artifact in artifacts
            if artifact.get("type") == "PROJECT"
        ]


        active = [
            project
            for project in projects
            if project.get("status") != "ARCHIVED"
        ]


        return DashboardReport(
            total_artifacts=len(artifacts),
            active_projects=len(active),
            health_issues=len(issues),
            recommendations=recommendations,
        )
