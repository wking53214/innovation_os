from innovation_os.lineage.builder import (
    ArtifactLineageBuilder,
)


def test_lineage_creation():

    builder = ArtifactLineageBuilder()

    link = builder.link(
        "CONVERSATION-001",
        "generated",
        "IDEA-001",
    )


    assert link.source_id == "CONVERSATION-001"
    assert link.target_id == "IDEA-001"



def test_forward_trace():

    builder = ArtifactLineageBuilder()

    builder.link(
        "IDEA-001",
        "implemented_by",
        "CODE-001",
    )


    results = builder.trace_forward(
        "IDEA-001"
    )


    assert len(results) == 1
    assert results[0].target_id == "CODE-001"



def test_backward_trace():

    builder = ArtifactLineageBuilder()

    builder.link(
        "PROJECT-001",
        "contains",
        "CODE-001",
    )


    results = builder.trace_backward(
        "CODE-001"
    )


    assert len(results) == 1
    assert results[0].source_id == "PROJECT-001"
