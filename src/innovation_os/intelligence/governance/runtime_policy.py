from dataclasses import dataclass, field


@dataclass
class RuntimePolicy:
    """
    Defines runtime intelligence execution constraints.
    """

    name: str = "default"
    allowed_operations: list[str] = field(
        default_factory=list
    )
    blocked_operations: list[str] = field(
        default_factory=list
    )


    def allows(
        self,
        operation: str
    ) -> bool:

        if operation in self.blocked_operations:
            return False

        if not self.allowed_operations:
            return True

        return operation in self.allowed_operations
