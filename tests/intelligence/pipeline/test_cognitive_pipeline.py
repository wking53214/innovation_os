from innovation_os.intelligence.pipeline import CognitivePipeline


def test_cognitive_pipeline():

    pipeline = CognitivePipeline()

    pipeline.register(
        lambda x: x * 2
    )

    assert pipeline.process(5) == 10
