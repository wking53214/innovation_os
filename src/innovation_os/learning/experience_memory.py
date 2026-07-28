class ExperienceMemory:


    def __init__(self):

        self.experiences = []


    def store(
        self,
        experience
    ):

        self.experiences.append(
            experience
        )


    def recall(self):

        return self.experiences
