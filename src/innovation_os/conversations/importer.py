from dataclasses import dataclass
from typing import List


@dataclass
class ConversationArtifact:

    conversation_id: str
    messages: List[str]
    keywords: List[str]



class ConversationImporter:


    def parse(
        self,
        conversation_id: str,
        content: str,
    ):

        messages = [
            line.strip()
            for line in content.splitlines()
            if line.strip()
        ]


        keywords = self.extract_keywords(
            content
        )


        return ConversationArtifact(
            conversation_id,
            messages,
            keywords,
        )



    def extract_keywords(
        self,
        content: str,
    ):

        terms = [
            "AI",
            "governance",
            "architecture",
            "code",
            "system",
            "idea",
            "project",
        ]


        return [
            term
            for term in terms
            if term.lower()
            in content.lower()
        ]
