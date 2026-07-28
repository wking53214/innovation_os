from innovation_os.intelligence.contracts import Observation


class PerceptionEngine:
    name = "perception_engine"

    def process(self, observation: Observation):

        return {
            "type": "perception",
            "subject": observation.subject,
            "features": observation.data,
            "confidence": observation.confidence,
        }
