from src.innovation_os.config.settings import (
    SettingsLoader,
)



def test_default_settings():

    settings = SettingsLoader().load()


    assert (
        settings.environment
        ==
        "development"
    )


    assert (
        settings.debug
        ==
        False
    )
