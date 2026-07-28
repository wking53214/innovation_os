from innovation_os.improvement import ImprovementProposal


class ImprovementAnalyzer:


    def analyze(
        self,
        observation
    ):

        if observation.value < 0.5:

            return ImprovementProposal(
                target_component=
                observation.component,

                recommendation=
                "optimize performance",

                confidence=0.85,
            )


        return ImprovementProposal(
            target_component=
            observation.component,

            recommendation=
            "maintain current state",

            confidence=0.60,
        )
