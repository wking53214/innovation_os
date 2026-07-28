from .factory import create_application


class ApplicationRuntime:

    def __init__(self):

        bundle = create_application()

        self.settings = bundle["settings"]

        self.system = bundle["system"]


    def run(
        self,
        payload,
        objective=None,
    ):

        return self.system.execute(
            key="runtime_execution",
            payload=payload,
            objective=objective,
        )
