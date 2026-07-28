from dataclasses import dataclass, field
import uuid


@dataclass
class TenantIdentity:

    tenant_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )

    name: str = ""

    metadata: dict = field(
        default_factory=dict
    )
