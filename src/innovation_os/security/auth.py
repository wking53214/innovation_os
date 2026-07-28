from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class AuthResult:

    authenticated: bool

    identity: str

    timestamp: datetime


class AuthenticationService:


    def __init__(self):

        self.tokens = {
            "innovation-os-demo-token":
            "system"
        }


    def authenticate(
        self,
        token
    ):

        identity = self.tokens.get(
            token
        )

        return AuthResult(
            authenticated=identity is not None,
            identity=identity or "unknown",
            timestamp=datetime.now(
                timezone.utc
            ),
        )
