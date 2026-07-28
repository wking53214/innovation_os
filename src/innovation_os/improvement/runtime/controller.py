class ImprovementController:


    def approve(
        self,
        proposal
    ):

        if proposal.confidence >= 0.8:

            proposal.approved = True


        return proposal
