from innovation_os.personal_system.builder import (
    PersonalSystemBuilder,
)


def test_system_build():

    builder = PersonalSystemBuilder()


    builder.add_node(
        "PROJECT-SENTINEL",
        "PROJECT",
        "Sentinel OS",
    )


    builder.add_node(
        "CODE-GSA",
        "CODE",
        "Governance Engine",
    )


    builder.connect(
        "PROJECT-SENTINEL",
        "implemented_by",
        "CODE-GSA",
    )


    graph = builder.ecosystem()


    assert len(graph["nodes"]) == 2
    assert len(graph["relationships"]) == 1



def test_category_lookup():

    builder = PersonalSystemBuilder()


    builder.add_node(
        "IDEA-001",
        "IDEA",
        "AI Governance",
    )


    results = builder.find_category(
        "IDEA"
    )


    assert len(results) == 1
