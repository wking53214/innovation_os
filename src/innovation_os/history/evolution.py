from dataclasses import dataclass
from datetime import datetime
from typing import List



@dataclass
class EvolutionEvent:

    item_id: str

    event_type: str

    description: str

    timestamp: datetime



class InnovationEvolutionEngine:


    def __init__(self):

        self.events: List[EvolutionEvent] = []



    def record(
        self,
        item_id: str,
        event_type: str,
        description: str,
        timestamp: datetime,
    ):

        event = EvolutionEvent(
            item_id=item_id,
            event_type=event_type,
            description=description,
            timestamp=timestamp,
        )

        self.events.append(
            event
        )

        return event



    def history(
        self,
        item_id: str,
    ):

        return sorted(
            [
                event
                for event in self.events
                if event.item_id == item_id
            ],
            key=lambda x: x.timestamp,
        )



    def attach_to_graph(
        self,
        graph,
        item_id: str,
    ):

        history = self.history(
            item_id
        )


        for event in history:

            event_id = (
                f"EVENT-{len(graph.nodes)+1:05d}"
            )


            graph.add_node(
                event_id,
                "EVENT",
                event_type=event.event_type,
                description=event.description,
            )


            graph.connect(
                item_id,
                event_id,
                "HAS_HISTORY",
            )


        return history
