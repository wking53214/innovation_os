from dataclasses import dataclass, field
from typing import Any, Dict, List



@dataclass
class MemoryResult:

    query: str

    artifacts: List[Any] = field(
        default_factory=list
    )

    history: List[Any] = field(
        default_factory=list
    )

    decisions: List[Any] = field(
        default_factory=list
    )

    provenance: List[Any] = field(
        default_factory=list
    )



class InnovationMemory:


    def __init__(
        self,
        registry=None,
        timeline=None,
        decisions=None,
        provenance=None,
    ):

        self.registry = registry

        self.timeline = timeline

        self.decisions = decisions

        self.provenance = provenance



    def query(
        self,
        term: str,
    ):

        result = MemoryResult(
            query=term
        )


        if self.registry:

            for artifact in self.registry.list_all():

                searchable = (
                    artifact.name
                    +
                    " "
                    +
                    artifact.artifact_id
                ).lower()


                if term.lower() in searchable:

                    result.artifacts.append(
                        artifact
                    )



        if self.timeline:

            result.history.extend(
                self.timeline.events
            )



        if self.decisions:

            result.decisions.extend(
                self.decisions.all()
            )



        if self.provenance:

            for records in self.provenance.records.values():

                result.provenance.extend(
                    records
                )


        return result
