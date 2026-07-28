from datetime import datetime, timezone


class IntelligenceLogger:


    def __init__(self):

        self.entries = []


    def log(
        self,
        level,
        message,
        metadata=None
    ):

        entry = {
            "level": level,
            "message": message,
            "metadata": metadata or {},
            "timestamp": datetime.now(
                timezone.utc
            ),
        }

        self.entries.append(
            entry
        )

        return entry


    def info(
        self,
        message,
        metadata=None
    ):

        return self.log(
            "INFO",
            message,
            metadata
        )


    def error(
        self,
        message,
        metadata=None
    ):

        return self.log(
            "ERROR",
            message,
            metadata
        )


    def history(
        self
    ):

        return self.entries
