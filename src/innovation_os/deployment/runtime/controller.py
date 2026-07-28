class DeploymentController:


    def deploy(
        self,
        plan,
        environment
    ):

        if not plan.approved:

            return False


        environment.status = (
            "deployed"
        )


        return True
