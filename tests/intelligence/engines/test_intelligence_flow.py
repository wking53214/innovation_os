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

    assert observation.source == "test"
    assert observation.subject == "event"
    assert observation.data == {"value": 1}

    assert perception["subject"] == "event"
    assert perception["features"] == {"value": 1}

    assert context["context"] is perception

    assert knowledge["knowledge"] is context

    assert evidence.content is knowledge
    assert evidence.source == "knowledge_engine"

    assert confidence.validate()

    assert hypothesis.supporting_data["evidence"] is evidence

    assert inference.conclusion == hypothesis.statement
    assert inference.confidence == hypothesis.confidence
    assert inference.reasoning["hypothesis"] is hypothesis
