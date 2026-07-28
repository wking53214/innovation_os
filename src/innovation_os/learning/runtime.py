from innovation_os.experience.event import ExperienceEvent
from innovation_os.experience.store import ExperienceStore
from innovation_os.evaluation.engine import EvaluationEngine
from innovation_os.learning.model import AdaptiveModel
from innovation_os.adaptation.engine import AdaptationEngine


class LearningRuntime:


    def __init__(self):

        self.experiences = ExperienceStore()

        self.evaluator = EvaluationEngine()

        self.model = AdaptiveModel()

        self.adapter = AdaptationEngine(
            self.model
        )


    def learn(
        self,
        agent_id,
        strategy,
        result
    ):

        reward = self.evaluator.evaluate(
            result
        )

        event = ExperienceEvent(
            agent_id=agent_id,
            action=strategy,
            outcome=result,
            reward=reward
        )

        self.experiences.record(
            event
        )

        return self.adapter.adapt(
            strategy,
            reward
        )
