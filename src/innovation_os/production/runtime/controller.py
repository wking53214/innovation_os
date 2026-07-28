from innovation_os.production import RuntimeState


class RuntimeController:


    def start(
        self,
        service
    ):

        return RuntimeState(
            service=service,
            status="running",
            health="unknown",
        )



    def stop(
        self,
        state
    ):

        state.status = "stopped"

        return state
