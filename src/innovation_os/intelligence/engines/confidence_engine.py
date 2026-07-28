from innovation_os.intelligence.contracts import Confidence


class ConfidenceEngine:
    name = "confidence_engine"

    def process(self, evidence):

        return Confidence(
            score=0.5,
            rationale="Default intelligence confidence estimate",
        )
