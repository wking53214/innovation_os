from innovation_os.intelligence.bootstrap import (
    bootstrap_intelligence,
)



class DummyPipeline:

    def process(
        self,
        data,
        context
    ):

        return data



def test_bootstrap():

    kernel = bootstrap_intelligence(
        DummyPipeline()
    )


    assert (
        kernel.resolve(
            "intelligence_system"
        )
        is not None
    )
