class SLAMonitor:


    def evaluate(
        self,
        sla
    ):

        return (
            sla.current_uptime
            >=
            sla.target_uptime
        )
