class ReasoningExchangeStore:


    def __init__(self):

        self.results = {}



    def publish(
        self,
        result
    ):

        self.results[
            result.reasoning_id
        ] = result


        return result



    def find(
        self,
        subject
    ):

        return [

            result

            for result
            in self.results.values()

            if result.subject
            ==
            subject

        ]
