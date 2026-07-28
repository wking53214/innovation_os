from dataclasses import dataclass


@dataclass
class TrustBoundary:

    source_tenant: str = ""

    target_tenant: str = ""

    trust_level: str = "restricted"

    approved: bool = False
