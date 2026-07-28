from innovation_os.interfaces import (
    IntelligenceRequest,
    IntelligenceResponse,
)


class AnalysisWorkflow:

    def __init__(self, application=None):

        self.application = application


    def execute(
        self,
        request: IntelligenceRequest,
    ):

        if self.application is None:
            from innovation_os.application.intelligence_application import (
                IntelligenceApplication
            )

            self.application = IntelligenceApplication()


        artifact = self.application.analyze(
            payload=request.input,
            context=request.context,
            objective=request.objective,
        )


        return IntelligenceResponse(
            artifact=artifact,
            confidence=getattr(
                artifact,
                "confidence",
                0.0,
            ),
        )
