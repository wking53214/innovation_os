from dataclasses import dataclass
from typing import List


@dataclass
class ConversationInsight:

    insight_type: str
    content: str
    source: str


class ConversationParser:


    def __init__(self):

        self.insights = []


    def parse(
        self,
        text: str,
        source: str,
    ):

        results = []

        lines = text.splitlines()

        for line in lines:

            clean = line.strip()

            if not clean:
                continue


            lowered = clean.lower()


            if "problem" in lowered:

                results.append(
                    ConversationInsight(
                        "PROBLEM",
                        clean,
                        source,
                    )
                )


            elif "idea" in lowered:

                results.append(
                    ConversationInsight(
                        "IDEA",
                        clean,
                        source,
                    )
                )


            elif "decision" in lowered:

                results.append(
                    ConversationInsight(
                        "DECISION",
                        clean,
                        source,
                    )
                )


            elif "architecture" in lowered:

                results.append(
                    ConversationInsight(
                        "CONCEPT",
                        clean,
                        source,
                    )
                )


        self.insights.extend(results)

        return results
