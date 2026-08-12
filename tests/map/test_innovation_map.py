from innovation_os.map.innovation_map import (
    InnovationMap,
)


def test_map_nodes():

    innovation_map = InnovationMap()

    innovation_map.add_node(
        "PROJECT-001",
        "PROJECT",
        "Sentinel OS",
    )

    node = innovation_map.get_node(
        "PROJECT-001"
    )

    assert node.label == "Sentinel OS"


def test_map_relationships():

    innovation_map = InnovationMap()

    innovation_map.add_node(
        "PROJECT-001",
        "PROJECT",
        "Sentinel OS",
    )

    innovation_map.add_node(
        "CODE-001",
        "CODE",
        "Governance Engine",
    )

    innovation_map.connect(
        "PROJECT-001",
        "CODE-001",
        "IMPLEMENTED_BY",
    )


    links = innovation_map.get_connections(
        "PROJECT-001"
    )

    assert len(links) == 1
    assert links[0].relationship == "IMPLEMENTED_BY"
