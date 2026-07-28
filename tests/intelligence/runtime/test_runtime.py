from innovation_os.intelligence.runtime import (
    ExecutionContext,
    IntelligenceSession,
)


def test_context():

    context = ExecutionContext(
        "session-1"
    )

    assert context.session_id == "session-1"



def test_session():

    session = IntelligenceSession(
        ExecutionContext(
            "s"
        )
    )

    session.add(
        "artifact"
    )

    assert len(session.artifacts) == 1
