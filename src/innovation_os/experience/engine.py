from innovation_os.knowledge import KnowledgeStore
from innovation_os.patterns import PatternDetector


class ExperienceEngine:


    def __init__(self):

        self.memory = KnowledgeStore()

        self.patterns = PatternDetector()



    def learn(
        self,
        key,
        artifact,
    ):

        detected = self.patterns.detect(
            artifact
        )

        return self.memory.add(
            key=key,
            content=artifact,
            metadata={
                "patterns": detected
            },
        )



    def recall(
        self,
        key,
    ):

        return self.memory.get(
            key
        )
