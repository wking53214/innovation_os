from dataclasses import dataclass, field


@dataclass
class ExecutionContext:

    session_id: str

    metadata: dict = field(
        default_factory=dict
    )
