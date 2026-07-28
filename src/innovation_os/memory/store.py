from typing import Any, Dict


class IntelligenceMemory:

    def __init__(self):
        self.records = {}


    def store(
        self,
        key: str,
        value: Any,
    ):

        self.records[key] = value


    def retrieve(
        self,
        key: str,
    ):

        return self.records.get(key)


    def all(self):

        return dict(
            self.records
        )
