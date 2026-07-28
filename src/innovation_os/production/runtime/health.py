class HealthMonitor:


    def check(
        self,
        state
    ):

        if state.status == "running":

            state.health = "healthy"

        else:

            state.health = "unhealthy"


        return state.health
