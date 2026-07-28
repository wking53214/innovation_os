from dataclasses import dataclass
from innovation_os.intelligence.contracts import IntelligenceArtifact


@dataclass
class IntelligenceRuntime:

    pipeline: object

    memory: object



    def _normalize(
        self,
        result
    ):

        if hasattr(
            result,
            "artifact_id"
        ):

            return result


        return IntelligenceArtifact(
            intelligence_type="runtime_result",
            source_system="intelligence_runtime",
            confidence=1.0,
            metadata={
                "payload": result
            },
        )



    def execute(
        self,
        input_data,
        context
    ):

        result = self.pipeline.process(
            input_data,
            context
        )


        artifact = self._normalize(
            result
        )


        self.memory.remember(
            artifact
        )


        return result
