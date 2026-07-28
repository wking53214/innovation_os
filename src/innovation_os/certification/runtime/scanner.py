from innovation_os.certification import CertificationReport


class ArchitectureScanner:


    def scan(
        self,
        components
    ):

        score = (
            len(components)
            /
            20
        )

        if score > 1:
            score = 1


        return CertificationReport(
            system="innovation-os",
            checks=components,
            passed=True,
            score=score,
        )
