from innovation_os.enterprise.models import (
    EnterpriseArtifact,
)



class EnterpriseAdapter:


    source_system = "unknown"



    def normalize(
        self,
        payload: dict
    ):

        raise NotImplementedError



    def ingest(
        self,
        payload: dict
    ):

        normalized = self.normalize(
            payload
        )


        return EnterpriseArtifact(
            source_system=self.source_system,
            artifact_type="ENTERPRISE_DATA",
            payload=normalized,
        )
