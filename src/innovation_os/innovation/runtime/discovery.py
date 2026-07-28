from innovation_os.innovation import InnovationHypothesis


class DiscoveryEngine:


    def generate(
        self,
        observation,
        evidence=None
    ):

        return InnovationHypothesis(
            statement=observation,
            confidence=0.75,
            evidence=evidence or [],
        )
