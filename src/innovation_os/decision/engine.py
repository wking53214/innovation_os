from .result import DecisionResult


class DecisionEngine:


    def __init__(self):

        self.decisions = []



    def create_decision(
        self,
        problem=None,
        selected_option=None,
        rejected_options=None,
        assumptions=None,
        confidence=0.0,
        approval="",
        decision_id=None,
        problem_id=None,
        context="",
        options=None,
        **kwargs,
    ):

        decision = DecisionResult(
            decision_id=decision_id or "",
            problem_id=problem_id or problem or "",
            context=context,
            options=options or [],
            selected_option=selected_option,
            rejected_options=rejected_options or [],
            assumptions=assumptions or [],
            confidence=confidence,
            approval=approval,
            decision=selected_option,
            rationale=approval,
        )


        self.decisions.append(
            decision
        )


        return decision



    def get_decision(
        self,
        decision_id,
    ):

        for decision in self.decisions:

            if decision.decision_id == decision_id:
                return decision

        return None



    def retrieve_decision(
        self,
        problem,
    ):

        for decision in self.decisions:

            if (
                decision.problem_id == problem
                or decision.context == problem
            ):
                return decision

        return None



    def get_decisions_for_problem(
        self,
        problem,
    ):

        return [
            decision
            for decision in self.decisions
            if (
                decision.problem_id == problem
                or decision.context == problem
            )
        ]



    def decide(
        self,
        reasoning,
    ):

        return DecisionResult(
            decision="analysis_complete",
            confidence=reasoning.confidence,
            rationale="Generated from intelligence reasoning pipeline",
        )
