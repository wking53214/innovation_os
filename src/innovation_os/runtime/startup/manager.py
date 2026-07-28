from datetime import datetime, timezone


class StartupManager:


    def __init__(self):

        self.started = False

        self.timestamp = None


    def start(self):

        self.started = True

        self.timestamp = datetime.now(
            timezone.utc
        )

        return {
            "status": "started",
            "timestamp": self.timestamp,
        }


    def stop(self):

        self.started = False

        return {
            "status": "stopped"
        }
