from dataclasses import dataclass


@dataclass
class AuditAdapter:
    """
    Audit integration boundary.
    """

    audit=None


    def log(
        self,
        event
    ):

        if self.audit and hasattr(
            self.audit,
            "log"
        ):
            return self.audit.log(
                event
            )

        return event
