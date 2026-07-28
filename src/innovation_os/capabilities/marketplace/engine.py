from .evaluation import CapabilityEvaluation



class CapabilityEvaluationEngine:


    def __init__(
        self
    ):

        self.evaluations = {}



    def evaluate(
        self,
        capability,
        quality,
        trust,
        compatibility
    ):

        evaluation = CapabilityEvaluation(
            capability_id=capability.capability_id,
            quality_score=quality,
            trust_score=trust,
            compatibility_score=compatibility,
        )


        evaluation.approved = (
            evaluation.overall_score()
            >=
            0.80
        )


        self.evaluations[
            capability.capability_id
        ] = evaluation


        return evaluation



    def get(
        self,
        capability_id
    ):

        return self.evaluations.get(
            capability_id
        )
