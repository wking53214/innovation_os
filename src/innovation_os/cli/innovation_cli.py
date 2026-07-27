from dataclasses import asdict



class InnovationCLI:


    def __init__(
        self,
        search=None,
        dashboard=None,
    ):

        self.search_engine = search
        self.dashboard = dashboard



    def search(
        self,
        query: str,
    ):

        if not self.search_engine:

            return []


        result = self.search_engine.search(
            query
        )


        return result.matches



    def status(self):

        return {

            "status": "READY",

            "components": [

                "Registry",

                "Timeline",

                "Memory",

                "Search",

                "Provenance",

            ],
        }



    def snapshot(
        self,
        item_id,
        name,
        memory_result,
    ):

        if not self.dashboard:

            return None


        return self.dashboard.build(
            item_id,
            name,
            memory_result,
        )
