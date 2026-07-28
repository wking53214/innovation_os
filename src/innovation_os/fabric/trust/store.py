class TrustStore:


    def __init__(self):

        self.records = {}



    def store(
        self,
        record
    ):

        self.records[
            record.node_id
        ] = record


        return record



    def get(
        self,
        node_id
    ):

        return self.records.get(
            node_id
        )
