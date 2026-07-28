from innovation_os.application import IntelligenceSystem
from innovation_os.config import IntelligenceSettings


def create_application():

    settings = IntelligenceSettings()

    system = IntelligenceSystem()

    return {
        "settings": settings,
        "system": system,
    }
