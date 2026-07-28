from innovation_os.intelligence.config import (
    IntelligenceSettings,
)


def test_settings():

    settings = IntelligenceSettings()

    assert settings.enabled
    assert settings.confidence_threshold > 0
