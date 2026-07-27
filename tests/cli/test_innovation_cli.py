from src.innovation_os.cli.innovation_cli import (
    InnovationCLI,
)



def test_cli_status():

    cli = InnovationCLI()


    result = cli.status()


    assert (
        result["status"]
        ==
        "READY"
    )


    assert (
        "Registry"
        in
        result["components"]
    )



class FakeSearch:


    class Result:

        matches = [
            "Sentinel"
        ]


    def search(
        self,
        query,
    ):

        return self.Result()



def test_cli_search():

    cli = InnovationCLI(
        search=FakeSearch()
    )


    result = cli.search(
        "Sentinel"
    )


    assert (
        "Sentinel"
        in
        result
    )
