class BenchmarkSuite:


    def __init__(self):

        self.tests = []


    def register(
        self,
        name,
        function
    ):

        self.tests.append(
            {
                "name": name,
                "function": function,
            }
        )


    def run(self):

        results = []

        for test in self.tests:

            results.append(
                {
                    "name": test["name"],
                    "result":
                    test["function"]()
                }
            )

        return results
