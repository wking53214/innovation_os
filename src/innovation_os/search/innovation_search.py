from dataclasses import dataclass
from typing import Any, List



@dataclass
class SearchResult:

    query: str

    matches: List[Any]



class InnovationSearch:


    def __init__(
        self,
        memory,
    ):

        self.memory = memory



    def search(
        self,
        query: str,
    ):

        memory_result = self.memory.query(
            query
        )


        matches = []


        matches.extend(
            memory_result.artifacts
        )

        matches.extend(
            memory_result.history
        )

        matches.extend(
            memory_result.decisions
        )

        matches.extend(
            memory_result.provenance
        )


        return SearchResult(
            query=query,
            matches=matches,
        )
