from dataclasses import dataclass
from typing import List



@dataclass
class QueryResult:

    intent: str
    matches: List[str]
    explanation: str



class NaturalLanguageInterface:


    def __init__(self):

        self.items = {}



    def add(
        self,
        item_id: str,
        description: str,
    ):

        self.items[item_id] = description.lower()



    def query(
        self,
        question: str,
    ) -> QueryResult:

        text = question.lower()


        if (
            "duplicate" in text
            or
            "similar" in text
        ):

            intent = "FIND_SIMILAR"


        elif (
            "next" in text
            or
            "recommend" in text
        ):

            intent = "RECOMMEND"


        elif (
            "connected" in text
            or
            "related" in text
        ):

            intent = "FIND_CONNECTIONS"


        else:

            intent = "SEARCH"



        matches = []


        stop_words = {
            "what",
            "which",
            "where",
            "when",
            "does",
            "projects",
            "project",
            "involve",
            "show",
            "find",
            "the",
            "and",
            "for",
        }


        words = [
            word.strip("?.,!")
            for word in text.split()
            if word.strip("?.,!") not in stop_words
        ]


        for item_id, description in self.items.items():

            if any(
                word.lower() in description
                for word in words
            ):

                matches.append(
                    item_id
                )


        return QueryResult(
            intent,
            matches,
            f"Detected intent: {intent}",
        )
