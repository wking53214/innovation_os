from innovation_os.api.server import (
    InnovationAPI,
)


def test_api_status():

    api = InnovationAPI()

    result = api.status()

    assert result["status"] == "operational"


def test_api_node_creation():

    api = InnovationAPI()

    node = api.add_node(
        "IDEA-001",
        "IDEA",
        "Governance Platform",
    )

    assert node["id"] == "IDEA-001"


def test_api_search():

    api = InnovationAPI()

    api.add_node(
        "IDEA-002",
        "IDEA",
        "AI Governance System",
    )

    results = api.search_nodes(
        "Governance"
    )

    assert len(results) == 1
