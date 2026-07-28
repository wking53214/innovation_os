class IncidentManager:


    def __init__(self):

        self.incidents = []



    def create(
        self,
        incident
    ):

        self.incidents.append(
            incident
        )

        return incident



    def active(
        self
    ):

        return [

            item

            for item in self.incidents

            if item.status == "open"

        ]
