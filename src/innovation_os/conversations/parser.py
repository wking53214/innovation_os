from dataclasses import dataclass
from pathlib import Path
from typing import List
import hashlib


@dataclass
class ConversationArtifact:

    conversation_id: str
    source_path: str
    title: str
    content_length: int



class ConversationParser:


    def __init__(self):

        self.conversations = []


    def parse_file(
        self,
        file_path: str,
    ):

        path = Path(file_path)

        content = path.read_text(
            errors="ignore"
        )


        artifact = ConversationArtifact(
            self._create_id(path),
            str(path),
            self._extract_title(content),
            len(content),
        )


        self.conversations.append(
            artifact
        )


        return artifact



    def _create_id(
        self,
        path: Path,
    ):

        digest = hashlib.sha256(
            str(path).encode()
        ).hexdigest()[:12]

        return (
            "CONVERSATION-"
            + digest
        )


    def _extract_title(
        self,
        content: str,
    ):

        for line in content.splitlines():

            if line.strip():

                return line.strip()[:80]


        return "Untitled Conversation"
