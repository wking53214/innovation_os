from dataclasses import dataclass


@dataclass
class IntelligenceSettings:

    environment: str = "development"

    debug: bool = False

    system_name: str = "innovation_os"

    version: str = "v2"

    confidence_threshold: float = 0.5

    governance_enabled: bool = True

    memory_enabled: bool = True



class SettingsLoader:


    def load(self):

        return IntelligenceSettings()



CONFIG = IntelligenceSettings()
