from innovation_os.conversations.importer import (
    ConversationImporter,
)


def test_conversation_parsing():

    importer = ConversationImporter()


    result = importer.parse(
        "CONVERSATION-001",
        """
        Need AI governance architecture.
        Build system and code.
        """,
    )


    assert (
        result.conversation_id
        ==
        "CONVERSATION-001"
    )


    assert "AI" in result.keywords
    assert "architecture" in result.keywords



def test_message_extraction():

    importer = ConversationImporter()


    result = importer.parse(
        "CHAT-001",
        """
        First message
        Second message
        """,
    )


    assert len(
        result.messages
    ) == 2
