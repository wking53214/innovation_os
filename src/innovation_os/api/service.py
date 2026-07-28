from innovation_os.interfaces import IntelligenceRequest
from innovation_os.workflows.analysis_workflow import AnalysisWorkflow
from innovation_os.application.intelligence_application import IntelligenceApplication


class IntelligenceService:


    def __init__(self):

        self.workflow = AnalysisWorkflow(
            application=IntelligenceApplication()
        )


    def analyze(
        self,
        payload,
        context=None,
        objective=None,
    ):

        request = IntelligenceRequest(
            input=payload,
            context=context,
            objective=objective,
        )

        return self.workflow.execute(
            request
        )
