from innovation_os.intelligence.pipeline import IntelligencePipeline


class Stage:

    def process(self, value):
        return value + 1


def test_pipeline_execution():

    pipeline = IntelligencePipeline()

    pipeline.add_stage(
        Stage()
    )

    result = pipeline.execute(1)

    assert result == 2
