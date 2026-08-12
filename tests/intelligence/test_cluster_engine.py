from innovation_os.intelligence.cluster_engine import (
    IdeaClusterEngine,
)



def test_cluster_creation():

    engine = IdeaClusterEngine()


    engine.add(
        "PROJECT-SENTINEL",
        [
            "AI",
            "governance",
            "security",
        ],
    )


    engine.add(
        "PROJECT-GSA",
        [
            "AI",
            "governance",
            "approval",
        ],
    )


    clusters = engine.cluster()


    assert len(clusters) == 1
    assert "PROJECT-SENTINEL" in clusters[0].members
    assert "PROJECT-GSA" in clusters[0].members
