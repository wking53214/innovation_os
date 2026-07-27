from src.innovation_os.search.interface import (
    InnovationSearch,
)

from src.innovation_os.timeline.engine import (
    TimelineEngine,
)



class InnovationOS:


    def __init__(self):

        self.search = InnovationSearch()
        self.timeline = TimelineEngine()



    def status(self):

        return {
            "system": "Innovation OS",
            "status": "READY",
            "components": [
                "Registry",
                "Timeline",
                "Map",
                "Narrative",
                "Search",
            ],
        }



    def search_items(
        self,
        query: str,
    ):

        return self.search.search(
            query
        )
