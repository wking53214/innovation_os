from dataclasses import dataclass


@dataclass
class IntelligenceRuntime:

    pipeline: object
    memory: object


    def execute(
        self,
        input_data,
        context
    ):

        result = self.pipeline.process(
            input_data,
            context
        )

        self.memory.remember(
            result
        )

        return result
