from .session import IntelligenceSession


class IntelligenceOrchestrator:

    def __init__(
        self,
        application=None,
        governance=None,
        memory=None,
    ):
        self.application = application
        self.governance = governance
        self.memory = memory


    def execute(
        self,
        request
    ):

        session = IntelligenceSession()

        if self.governance:

            approved = self.governance.check(
                request
            )

            if not approved:
                return {
                    "status": "rejected",
                    "session": session.summary(),
                }


        if self.application:

            result = self.application.run(
                request
            )

            session.record_artifact(
                result
            )

        else:
            result = None


        if self.memory:

            self.memory.store(
                result
            )


        return {
            "status": "complete",
            "result": result,
            "session": session.summary(),
        }
