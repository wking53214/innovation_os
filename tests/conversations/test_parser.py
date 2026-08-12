import tempfile
from pathlib import Path

from innovation_os.conversations.parser import (
    ConversationParser,
)


def test_conversation_parser():

    with tempfile.TemporaryDirectory() as directory:

        file = Path(directory) / "chat.txt"

        file.write_text(
            "Building Innovation OS\n"
            "Need artifact tracking"
        )


        parser = ConversationParser()

        result = parser.parse_file(
            str(file)
        )


        assert result.conversation_id.startswith(
            "CONVERSATION-"
        )

        assert result.title == (
            "Building Innovation OS"
        )

        assert result.content_length > 0
