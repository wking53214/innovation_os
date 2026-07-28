from dataclasses import dataclass


@dataclass
class IntelligenceSystem:

    runtime: object

    memory: object

    governance: object = None

    telemetry: object = None


    def execute(
        self,
        input_data,
        context
    ):

        if self.governance:

            approved = self.governance.validate(
                input_data
            )

            if not approved:
                return None


        result = self.runtime.execute(
            input_data,
            context
        )


        if self.telemetry:

            self.telemetry.observe(
                result
            )


        return result
