from src.innovation_os.search.innovation_search import (
    InnovationSearch,
)


class FakeMemory:


    def query(
        self,
        value,
    ):

        class Result:

            artifacts = [
                "Sentinel Artifact"
            ]

            history = []

            decisions = []

            provenance = []


        return Result()



def test_innovation_search():

    search = InnovationSearch(
        FakeMemory()
    )


    result = search.search(
        "Sentinel"
    )


    assert (
        result.query
        ==
        "Sentinel"
    )


    assert (
        len(result.matches)
        ==
        1
    )
