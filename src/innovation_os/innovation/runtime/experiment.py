from innovation_os.innovation import InnovationExperiment


class ExperimentEngine:


    def create(
        self,
        hypothesis,
        objective
    ):

        return InnovationExperiment(
            hypothesis_id=
            hypothesis.hypothesis_id,

            objective=objective,
        )



    def evaluate(
        self,
        experiment,
        score
    ):

        experiment.score = score


        if score >= 0.8:

            experiment.result = "validated"

        else:

            experiment.result = "needs_review"


        return experiment
