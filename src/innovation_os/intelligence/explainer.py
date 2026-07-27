from dataclasses import dataclass



@dataclass
class InnovationExplanation:

    query: str

    artifacts: list

    history: list

    decisions: list

    provenance: list



class InnovationExplainer:


    def __init__(
        self,
        memory,
        search,
    ):

        self.memory = memory

        self.search = search



    def explain(
        self,
        query: str,
    ):

        memory = self.memory.query(
            query
        )


        return InnovationExplanation(

            query=query,

            artifacts=memory.artifacts,

            history=memory.history,

            decisions=memory.decisions,

            provenance=memory.provenance,

        )
