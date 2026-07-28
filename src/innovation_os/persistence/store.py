from .record import PersistentRecord


class PersistenceStore:


    def __init__(self):

        self.records = {}


    def save(
        self,
        key,
        value
    ):

        record = PersistentRecord(
            key=key,
            value=value
        )

        self.records[key] = record

        return record


    def load(
        self,
        key
    ):

        record = self.records.get(
            key
        )

        if record:

            return record.value

        return None


    def exists(
        self,
        key
    ):

        return key in self.records


    def all(
        self
    ):

        return list(
            self.records.values()
        )
