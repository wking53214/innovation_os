from innovation_os.intelligence.api import (
    IntelligenceService,
    IntelligenceRequest,
)


class FakeSystem:

    def process(self, payload):

        class Artifact:
            artifact_id = "test-id"
            confidence = .95

        return Artifact()



def test_intelligence_service():

    service = IntelligenceService(
        FakeSystem()
    )

    response = service.execute(
        IntelligenceRequest(
            payload={
                "signal": "test"
            }
        )
    )

    assert response.success
    assert response.confidence == .95
