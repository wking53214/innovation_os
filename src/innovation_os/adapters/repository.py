from .base import IntelligenceAdapter


class RepositoryAdapter(
    IntelligenceAdapter
):

    def __init__(
        self,
        repository
    ):
        self.repository = repository


    def name(self):

        return "repository"


    def execute(
        self,
        payload
    ):

        return self.repository.save(
            payload["key"],
            payload["value"]
        )
