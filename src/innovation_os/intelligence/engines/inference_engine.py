from innovation_os.intelligence.contracts import Inference


class InferenceEngine:
    name = "inference_engine"

    def process(self, hypothesis):

        return Inference(
            conclusion=hypothesis.statement,
            reasoning={
                "hypothesis": hypothesis
            },
            confidence=hypothesis.confidence,
        )
