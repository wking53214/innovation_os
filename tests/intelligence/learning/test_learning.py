from innovation_os.intelligence.learning import (
    FeedbackEngine,
    AdaptationEngine,
)


def test_learning_loop():

    feedback = FeedbackEngine()

    result = feedback.record(
        "artifact",
        "success",
        .9
    )

    adaptation = AdaptationEngine()

    output = adaptation.adapt(
        result
    )

    assert output
