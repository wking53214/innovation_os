from dataclasses import dataclass


@dataclass
class AccessControl:
    """
    Controls intelligence capability access.
    """

    role: str


    def can_execute(
        self,
        capability: str
    ) -> bool:

        if self.role == "admin":
            return True

        return capability != "restricted"
