from .record import TrustRecord



class FabricTrustEvaluator:


    def __init__(
        self,
        threshold=0.80
    ):

        self.threshold = threshold



    def evaluate(
        self,
        node
    ):

        score = min(
            1.0,
            len(node.capabilities)
            /
            10
            +
            0.5
        )


        return TrustRecord(
            node_id=node.node_id,
            trust_score=score,
            verified=(
                score >= self.threshold
            ),
            metadata={
                "organization":
                node.organization
            }
        )
