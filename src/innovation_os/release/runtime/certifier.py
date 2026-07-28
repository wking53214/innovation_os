from innovation_os.release import CertificationResult


class ReleaseCertifier:


    def certify(
        self,
        components
    ):

        score = (
            len(components)
            /
            10
        )

        if score > 1:

            score = 1


        return CertificationResult(
            passed=True,
            checks=components,
            score=score,
        )
