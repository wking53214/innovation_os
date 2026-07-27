from dataclasses import dataclass
from typing import List


@dataclass
class LineageLink:

    source_id: str
    relationship: str
    target_id: str



class ArtifactLineageBuilder:


    def __init__(self):

        self.links: List[LineageLink] = []


    def link(
        self,
        source_id: str,
        relationship: str,
        target_id: str,
    ):

        lineage = LineageLink(
            source_id,
            relationship,
            target_id,
        )

        self.links.append(
            lineage
        )

        return lineage



    def trace_forward(
        self,
        artifact_id: str,
    ):

        return [
            link
            for link in self.links
            if link.source_id == artifact_id
        ]



    def trace_backward(
        self,
        artifact_id: str,
    ):

        return [
            link
            for link in self.links
            if link.target_id == artifact_id
        ]
