from innovation_os.memory import IntelligenceMemory
from innovation_os.application.intelligence_application import IntelligenceApplication


class AnalysisService:

    def __init__(self):

        self.application = IntelligenceApplication()
        self.memory = IntelligenceMemory()


    def analyze_and_store(
        self,
        key,
        payload,
        context=None,
        objective=None,
    ):

        result = self.application.analyze(
            payload=payload,
            context=context,
            objective=objective,
        )

        self.memory.store(
            key,
            result,
        )

        return result


    def recall(
        self,
        key,
    ):

        return self.memory.retrieve(
            key
        )
