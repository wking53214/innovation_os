from innovation_os.intelligence.contracts import Hypothesis


class HypothesisEngine:
    name = "hypothesis_engine"

    def process(self, evidence):

        return Hypothesis(
            statement="Generated hypothesis",
            supporting_data={
                "evidence": evidence
            },
            confidence=0.5,
        )
