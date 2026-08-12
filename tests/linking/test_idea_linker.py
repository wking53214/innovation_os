from innovation_os.linking.idea_linker import (
    IdeaLinker,
)



def test_idea_artifact_linking():

    linker = IdeaLinker()


    linker.link(
        "IDEA-SENTINEL",
        "CODE-00001",
    )


    linker.link(
        "IDEA-SENTINEL",
        "CODE-00002",
    )


    assert (
        linker.artifacts_for(
            "IDEA-SENTINEL"
        )
        ==
        [
            "CODE-00001",
            "CODE-00002",
        ]
    )


    assert (
        linker.ideas_for_artifact(
            "CODE-00001"
        )
        ==
        [
            "IDEA-SENTINEL"
        ]
    )
