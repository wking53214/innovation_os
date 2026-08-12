from dataclasses import dataclass


from innovation_os.ideation.idea_extractor import (
    IdeaExtractor,
)



@dataclass
class ArtifactFixture:

    path: str
    content: str



def test_extract_ideas():

    artifact = ArtifactFixture(
        path="notes.md",
        content="""
        Sentinel OS uses GSA governance
        with knowledge graph architecture.
        """,
    )


    result = IdeaExtractor().extract(
        artifact
    )


    titles = [
        idea.title
        for idea in result
    ]


    assert "Sentinel OS" in titles

    assert (
        "Governed Secure AI Gateway"
        in titles
    )

    assert (
        "Knowledge Graph"
        in titles
    )
