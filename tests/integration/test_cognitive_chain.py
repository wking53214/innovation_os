from innovation_os.intelligence.bootstrap.default_kernel import (
    create_intelligence_kernel,
)
from innovation_os.intelligence.contracts import Signal


def test_full_cognitive_chain_through_kernel():
    """
    Exercises the real Observation -> Perception -> Context -> Knowledge
    -> Evidence -> Hypothesis -> Inference chain through the kernel built
    by create_intelligence_kernel(), using the actual registered engines
    rather than stand-in test doubles. This is the flow described in the
    README's intelligence runtime diagram, run end-to-end for the first
    time.
    """

    kernel = create_intelligence_kernel()

    signal = Signal(
        source="sensor",
        signal_type="temperature",
        payload={"value": 72},
    )

    observation = kernel.execute("observation", signal)
    assert observation.source == "sensor"
    assert observation.subject == "temperature"

    perception = kernel.execute("perception", observation)
    assert perception["type"] == "perception"
    assert perception["subject"] == "temperature"

    context = kernel.execute("context", perception)
    assert context["context"] == perception

    knowledge = kernel.execute("knowledge", context)
    assert knowledge["knowledge"] == context

    evidence = kernel.execute("evidence", knowledge)
    assert evidence.source == "knowledge_engine"
    assert evidence.content == knowledge

    hypothesis = kernel.execute("hypothesis", evidence)
    assert hypothesis.statement == "Generated hypothesis"

    inference = kernel.execute("inference", hypothesis)
    assert inference.conclusion == hypothesis.statement
    assert inference.confidence == hypothesis.confidence


def test_confidence_engine_runs_independently_on_evidence():
    """
    The confidence engine is registered alongside the main chain but
    isn't consumed by it downstream in the current wiring - this confirms
    it's independently callable against real Evidence output.
    """

    kernel = create_intelligence_kernel()

    signal = Signal(
        source="sensor",
        signal_type="temperature",
        payload={"value": 72},
    )

    observation = kernel.execute("observation", signal)
    perception = kernel.execute("perception", observation)
    context = kernel.execute("context", perception)
    knowledge = kernel.execute("knowledge", context)
    evidence = kernel.execute("evidence", knowledge)

    confidence = kernel.execute("confidence", evidence)
    assert 0.0 <= confidence.score <= 1.0
