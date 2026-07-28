from innovation_os.intelligence.bootstrap.default_kernel import (
    create_intelligence_kernel,
)

from innovation_os.intelligence.contracts import (
    Signal,
    IntelligenceArtifact,
)


class IntelligenceApplication:
    """
    Product-facing application layer.

    Executes requests through the Intelligence OS runtime.
    """

    def __init__(self):

        self.kernel = create_intelligence_kernel()


    def analyze(
        self,
        payload,
        context=None,
        objective=None,
    ):

        signal = Signal(
            source="innovation_os_application",
            signal_type="analysis",
            payload={
                "input": payload,
                "context": context,
                "objective": objective,
            },
        )


        observation = self.kernel.registry.get_engine(
            "observation"
        ).process(signal)


        perception = self.kernel.registry.get_engine(
            "perception"
        ).process(observation)


        context_result = self.kernel.registry.get_engine(
            "context"
        ).process(perception)


        knowledge = self.kernel.registry.get_engine(
            "knowledge"
        ).process(context_result)


        evidence = self.kernel.registry.get_engine(
            "evidence"
        ).process(knowledge)


        confidence = self.kernel.registry.get_engine(
            "confidence"
        ).process(evidence)


        hypothesis = self.kernel.registry.get_engine(
            "hypothesis"
        ).process(evidence)


        inference = self.kernel.registry.get_engine(
            "inference"
        ).process(hypothesis)


        return IntelligenceArtifact(
            intelligence_type="analysis",
            source_system="innovation_os_runtime",
            payload={
                "input": payload,
                "context": context,
                "objective": objective,
                "inference": inference,
            },
            observation=observation,
            confidence=confidence.score,
            metadata={
                "pipeline": [
                    "observation",
                    "perception",
                    "context",
                    "knowledge",
                    "evidence",
                    "confidence",
                    "hypothesis",
                    "inference",
                ]
            },
        )
