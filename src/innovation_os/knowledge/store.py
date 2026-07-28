from .record import KnowledgeRecord


class KnowledgeStore:


    def __init__(self):

        self.records = {}


    def add(
        self,
        key,
        content,
        metadata=None,
    ):

        record = KnowledgeRecord(
            key=key,
            content=content,
            metadata=metadata or {},
        )

        self.records[key] = record

        return record


    def get(
        self,
        key,
    ):

        return self.records.get(
            key
        )


    def search(
        self,
        term,
    ):

        results = []

        for record in self.records.values():

            if term.lower() in str(
                record.content
            ).lower():

                results.append(
                    record
                )

        return results
