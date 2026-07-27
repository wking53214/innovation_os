from src.innovation_os.conversations.parser import (
    ConversationParser,
)


def test_conversation_parser():

    parser = ConversationParser()

    results = parser.parse(
        """
        Problem: AI systems lack governance

        Idea: Create approval workflows

        Decision: Human review required
        """,
        "chat001",
    )


    assert len(results) == 3

    assert results[0].insight_type == "PROBLEM"
    assert results[1].insight_type == "IDEA"
    assert results[2].insight_type == "DECISION"


def test_conversation_source_tracking():

    parser = ConversationParser()

    result = parser.parse(
        "Idea: Knowledge operating system",
        "conversation01",
    )

    assert result[0].source == "conversation01"
