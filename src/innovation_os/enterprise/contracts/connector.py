from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid



@dataclass
class ConnectorIdentity:


    connector_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )


    name: str = ""

    provider: str = ""

    version: str = "1.0"


    metadata: dict = field(
        default_factory=dict
    )


    created_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )



class ConnectorContract:


    def connect(
        self
    ):

        raise NotImplementedError


    def disconnect(
        self
    ):

        raise NotImplementedError


    def health(
        self
    ):

        raise NotImplementedError
