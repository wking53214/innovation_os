from innovation_os.intelligence.kernel import (
    CognitiveKernel,
)

from innovation_os.intelligence.contracts import (
    Signal,
    Observation,
    Evidence,
    Confidence,
    Hypothesis,
    Inference,
    IntelligenceArtifact,
)

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

from innovation_os.intelligence.adapters import (
    PatternAdapter,
    ClusterAdapter,
    DuplicateAdapter,
    RepositoryAdapter,
)


def create_intelligence_kernel():

    kernel = CognitiveKernel()

    contracts = {
        "signal": Signal,
        "observation": Observation,
        "evidence": Evidence,
        "confidence": Confidence,
        "hypothesis": Hypothesis,
        "inference": Inference,
        "artifact": IntelligenceArtifact,
    }

    for name, contract in contracts.items():
        kernel.registry.register_contract(
            name,
            contract
        )


    engines = {
        "observation": ObservationEngine(),
        "perception": PerceptionEngine(),
        "context": ContextEngine(),
        "knowledge": KnowledgeEngine(),
        "evidence": EvidenceEngine(),
        "confidence": ConfidenceEngine(),
        "hypothesis": HypothesisEngine(),
        "inference": InferenceEngine(),
    }

    for name, engine in engines.items():
        kernel.register_engine(
            name,
            engine
        )


    adapters = {
        "pattern": PatternAdapter(),
        "cluster": ClusterAdapter(),
        "duplicate": DuplicateAdapter(),
        "repository": RepositoryAdapter(),
    }

    for name, adapter in adapters.items():
        kernel.register_adapter(
            name,
            adapter
        )


    return kernel
