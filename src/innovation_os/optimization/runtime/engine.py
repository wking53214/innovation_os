from innovation_os.optimization import (
    OptimizationProposal,
)


class OptimizationEngine:


    def analyze(
        self,
        metrics
    ):

        if not metrics:

            return OptimizationProposal(
                target="system",
                recommendation="No optimization required",
                confidence=0.0,
            )


        average = sum(
            item.value
            for item in metrics
        ) / len(metrics)



        if average < 0.5:

            return OptimizationProposal(
                target="runtime",
                recommendation="Increase resource allocation",
                confidence=0.85,
            )


        return OptimizationProposal(
            target="runtime",
            recommendation="Maintain current configuration",
            confidence=0.90,
        )
