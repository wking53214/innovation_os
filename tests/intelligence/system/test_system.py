from innovation_os.intelligence.system import (
    create_intelligence_system,
)


class DummyPipeline:


    def process(
        self,
        data,
        context
    ):

        return data



def test_system_bootstrap():

    system = create_intelligence_system(
        DummyPipeline()
    )


    result = system.execute(
        {
            "signal": "test"
        },
        {}
    )


    assert result["signal"] == "test"
