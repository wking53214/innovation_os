from innovation_os.intelligence.bootstrap import create_intelligence_kernel
from innovation_os.intelligence.contracts import IntelligenceArtifact


class IntelligenceApplication:
    """
    Product-facing application layer.

    Wraps Intelligence OS kernel capabilities into
    user-facing workflows.
    """

    def __init__(self):
        self.kernel = create_intelligence_kernel()


    def analyze(
        self,
        payload,
        context=None,
        objective=None,
    ):
        artifact = IntelligenceArtifact(
            intelligence_type="analysis",
            source_system="innovation_os_application",
            payload={
                "input": payload,
                "context": context,
                "objective": objective,
            },
            confidence=0.5,
        )

        return artifact
