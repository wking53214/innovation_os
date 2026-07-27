from src.innovation_os.personal_map.engine import (
    PersonalInnovationMap,
)



def test_personal_map_connections():

    graph = PersonalInnovationMap()


    graph.add_node(
        "PROJECT-001",
        "PROJECT",
        "Sentinel OS",
    )


    graph.add_node(
        "CODE-001",
        "CODE",
        "gsa_gateway.py",
    )


    graph.connect(
        "PROJECT-001",
        "CODE-001",
    )


    result = graph.get_connections(
        "PROJECT-001"
    )


    assert "CODE-001" in result



def test_project_view():

    graph = PersonalInnovationMap()


    graph.add_node(
        "PROJECT-001",
        "PROJECT",
        "Innovation OS",
    )


    result = graph.build_project_view(
        "PROJECT-001"
    )


    assert result["project"] == "PROJECT-001"
