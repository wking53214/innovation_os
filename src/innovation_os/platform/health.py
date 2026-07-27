from dataclasses import dataclass
from typing import Dict


@dataclass
class HealthStatus:

    component: str
    healthy: bool
    message: str



class SystemHealth:

    def __init__(self):

        self.checks = []


    def register(
        self,
        component: str,
        healthy: bool,
        message: str,
    ):

        status = HealthStatus(
            component,
            healthy,
            message,
        )

        self.checks.append(status)

        return status



    def report(self) -> Dict:

        return {
            item.component: item.healthy
            for item in self.checks
        }
