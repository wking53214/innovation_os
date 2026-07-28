import os
from dataclasses import dataclass


@dataclass
class RuntimeEnvironment:

    name: str

    debug: bool

    version: str


def load_environment():

    return RuntimeEnvironment(
        name=os.getenv(
            "INNOVATION_OS_ENV",
            "development"
        ),

        debug=os.getenv(
            "INNOVATION_OS_DEBUG",
            "false"
        ).lower() == "true",

        version=os.getenv(
            "INNOVATION_OS_VERSION",
            "2.0"
        ),
    )
