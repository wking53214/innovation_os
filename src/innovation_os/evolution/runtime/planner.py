class EvolutionPlanner:


    def create_plan(
        self,
        current_version,
        target_version,
        capabilities
    ):

        return {
            "from": current_version,
            "to": target_version,
            "capabilities": capabilities,
            "status": "planned",
        }
