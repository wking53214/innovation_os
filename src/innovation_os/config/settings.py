from dataclasses import dataclass
import os



@dataclass
class InnovationSettings:

    environment: str

    debug: bool

    project_root: str



class SettingsLoader:


    def load(self):

        return InnovationSettings(

            environment=os.getenv(
                "INNOVATION_ENV",
                "development",
            ),

            debug=os.getenv(
                "INNOVATION_DEBUG",
                "false",
            ).lower() == "true",

            project_root=os.getenv(
                "INNOVATION_ROOT",
                ".",
            ),
        )
