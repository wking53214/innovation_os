from dataclasses import dataclass


@dataclass
class Feedback:

    source: str

    score: float

    comments: str



class FeedbackEngine:


    def __init__(self):

        self.feedback = []


    def add(
        self,
        feedback
    ):

        self.feedback.append(
            feedback
        )


    def all(self):

        return self.feedback
