from dataclasses import dataclass


@dataclass
class CertificationResult:

    passed: bool = False

    checks: list = None

    score: float = 0.0
