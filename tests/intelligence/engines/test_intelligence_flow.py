from innovation_os.intelligence.contracts import Signal
from innovation_os.intelligence.engines import (
    ObservationEngine,
    PerceptionEngine,
    ContextEngine,
    KnowledgeEngine,
    EvidenceEngine,
    ConfidenceEngine,
    HypothesisEngine,
    InferenceEngine,
)


def test_intelligence_flow():

    signal = Signal(
        source="test",
        signal_type="event",
        payload={"value": 1},
    )

    observation = ObservationEngine().process(signal)
    perception = PerceptionEngine().process(observation)
    context = ContextEngine().process(perception)
    knowledge = KnowledgeEngine().process(context)
    evidence = EvidenceEngine().process(knowledge)
    confidence = ConfidenceEngine().process(evidence)
    hypothesis = HypothesisEngine().process(evidence)
    inference = InferenceEngine().process(hypothesis)

    assert observation
    assert perception
    assert context
    assert knowledge
    assert evidence
    assert confidence.validate()
    assert hypothesis
    assert inference
