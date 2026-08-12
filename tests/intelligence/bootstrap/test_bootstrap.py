from innovation_os.intelligence.bootstrap import (
    bootstrap_intelligence,
)
from innovation_os.intelligence.system import IntelligenceSystem



class DummyPipeline:

    def process(
        self,
        data,
        context
    ):

        return data



def test_bootstrap():

    pipeline = DummyPipeline()

    kernel = bootstrap_intelligence(
        pipeline
    )

    system = kernel.resolve(
        "intelligence_system"
    )

    assert isinstance(system, IntelligenceSystem)
    assert system.runtime.pipeline is pipeline

    result = system.execute(
        "payload",
        {"key": "value"},
    )

    assert result == "payload"
