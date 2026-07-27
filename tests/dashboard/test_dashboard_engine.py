from src.innovation_os.dashboard.engine import (
    InnovationDashboard,
)


def test_dashboard_generation():

    dashboard = InnovationDashboard()


    report = dashboard.generate(
        [
            {
                "id": "PROJECT-001",
                "type": "PROJECT",
                "status": "IMPLEMENTED",
            },
            {
                "id": "IDEA-001",
                "type": "IDEA",
            },
        ],
        [
            "ORPHAN_IDEA",
        ],
        [
            "Review IDEA-001",
        ],
    )


    assert report.total_artifacts == 2
    assert report.active_projects == 1
    assert report.health_issues == 1
    assert len(report.recommendations) == 1
