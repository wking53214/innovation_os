class ExperienceStore:


    def __init__(self):

        self.events = []


    def record(
        self,
        event
    ):

        self.events.append(
            event
        )


    def history(
        self,
        agent_id=None
    ):

        if agent_id is None:

            return self.events

        return [
            e for e in self.events
            if e.agent_id == agent_id
        ]
