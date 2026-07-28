class RecoveryManager:


    def recover(
        self,
        state
    ):

        if state.health == "unhealthy":

            state.status = "recovering"

            return True


        return False
