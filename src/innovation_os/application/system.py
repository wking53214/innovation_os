from innovation_os.application.services import AnalysisService
from innovation_os.governance import GovernanceGate
from innovation_os.observability import IntelligenceLogger
from innovation_os.reasoning import ReasoningEngine
from innovation_os.decision import DecisionEngine
from innovation_os.experience import ExperienceEngine


class IntelligenceSystem:

    def __init__(self):

        self.analysis = AnalysisService()
        self.governance = GovernanceGate()
        self.logger = IntelligenceLogger()
        self.reasoning = ReasoningEngine()
        self.decision = DecisionEngine()
        self.experience = ExperienceEngine()


    def execute(
        self,
        key,
        payload,
        objective=None,
    ):

        gate = self.governance.check(
            payload
        )

        self.logger.emit(
            "governance_check",
            gate,
        )

        if not gate["approved"]:
            return None


        result = self.analysis.analyze_and_store(
            key=key,
            payload=payload,
            objective=objective,
        )

        self.logger.emit(
            "analysis_complete",
            {
                "key": key,
            },
        )

        self.experience.learn(
            key,
            result.artifact,
        )

        reasoning = self.reasoning.evaluate(
            result.artifact
        )

        decision = self.decision.decide(
            reasoning
        )

        self.logger.emit(
            "decision_complete",
            {
                "decision": decision.decision
            },
        )

        return {
            "artifact": result,
            "reasoning": reasoning,
            "decision": decision,
        }
