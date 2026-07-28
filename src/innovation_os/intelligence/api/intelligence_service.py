from dataclasses import dataclass

from innovation_os.intelligence.api.request_models import (
    IntelligenceRequest,
)

from innovation_os.intelligence.api.response_models import (
    IntelligenceResponse,
)


@dataclass
class IntelligenceService:
    """
    Public service boundary for intelligence execution.
    """

    system: object


    def execute(
        self,
        request: IntelligenceRequest
    ):

        artifact = self.system.process(
            request.payload
        )


        return IntelligenceResponse(
            success=True,
            artifact_id=artifact.artifact_id,
            confidence=artifact.confidence,
            data={
                "source": request.source,
            },
        )
