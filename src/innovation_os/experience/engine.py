from .store import ExperienceStore
from .event import ExperienceEvent


class ExperienceEngine:

    def __init__(self):

        self.store = ExperienceStore()


    def record(
        self,
        agent_id,
        action,
        outcome,
        reward=0.0
    ):

        event = ExperienceEvent(
            agent_id=agent_id,
            action=action,
            outcome=outcome,
            reward=reward
        )

        self.store.record(
            event
        )

        return event


    def get_history(
        self,
        agent_id=None
    ):

        return self.store.history(
            agent_id
        )
