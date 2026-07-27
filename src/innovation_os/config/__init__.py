from .settings import (
    InnovationSettings,
    SettingsLoader,
)


CONFIG = SettingsLoader().load()


__all__ = [
    "CONFIG",
    "InnovationSettings",
    "SettingsLoader",
]
