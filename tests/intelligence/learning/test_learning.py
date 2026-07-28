from innovation_os.intelligence.learning import (
    MemoryEvent,
    FeedbackEngine,
    AdaptationEngine,
    LearningEngine,
)


def test_memory_event():

    event = MemoryEvent(
        "observation",
        {
            "value": 1
        }
    )

    assert event.event_type == "observation"



def test_feedback_engine():

    engine = FeedbackEngine()

    engine.record(
        "positive"
    )

    assert engine.latest() == "positive"



def test_adaptation_engine():

    engine = AdaptationEngine()

    result = engine.adapt(
        "feedback"
    )

    assert result["status"] == "adapted"



def test_learning_cycle():

    feedback = FeedbackEngine()

    adaptation = AdaptationEngine()

    learning = LearningEngine(
        feedback,
        adaptation,
    )

    result = learning.learn(
        "new_pattern"
    )

    assert result["status"] == "adapted"
    assert adaptation.count() == 1
