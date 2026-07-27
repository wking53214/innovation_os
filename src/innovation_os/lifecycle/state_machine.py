from dataclasses import dataclass
from typing import Dict, List


class LifecycleState:

    IDEA = "IDEA"
    VALIDATED = "VALIDATED"
    DESIGNED = "DESIGNED"
    IMPLEMENTED = "IMPLEMENTED"
    TESTING = "TESTING"
    DEPLOYED = "DEPLOYED"
    ARCHIVED = "ARCHIVED"



@dataclass
class LifecycleRecord:

    artifact_id: str
    state: str
    history: List[str]



class InnovationLifecycleEngine:


    VALID_TRANSITIONS = {

        "IDEA": [
            "VALIDATED"
        ],

        "VALIDATED": [
            "DESIGNED"
        ],

        "DESIGNED": [
            "IMPLEMENTED"
        ],

        "IMPLEMENTED": [
            "TESTING"
        ],

        "TESTING": [
            "DEPLOYED"
        ],

        "DEPLOYED": [
            "ARCHIVED"
        ],
    }


    def __init__(self):

        self.records: Dict[str, LifecycleRecord] = {}


    def create(
        self,
        artifact_id: str,
    ):

        record = LifecycleRecord(
            artifact_id,
            LifecycleState.IDEA,
            [
                LifecycleState.IDEA
            ],
        )

        self.records[artifact_id] = record

        return record


    def transition(
        self,
        artifact_id: str,
        new_state: str,
    ):

        record = self.records.get(
            artifact_id
        )

        if not record:
            return False


        allowed = self.VALID_TRANSITIONS.get(
            record.state,
            [],
        )


        if new_state not in allowed:

            return False


        record.state = new_state

        record.history.append(
            new_state
        )

        return True


    def get(
        self,
        artifact_id: str,
    ):

        return self.records.get(
            artifact_id
        )
