from dataclasses import dataclass, field
import hashlib


@dataclass
class ComponentIdentity:

    name: str = ""

    fingerprint: str = ""

    metadata: dict = field(
        default_factory=dict
    )


    def generate(
        self,
        content
    ):

        self.fingerprint = hashlib.sha256(
            content.encode()
        ).hexdigest()

        return self.fingerprint
