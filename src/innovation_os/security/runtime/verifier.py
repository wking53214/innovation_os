from innovation_os.security import TrustDecision


class ArtifactVerifier:


    def verify(
        self,
        identity,
        content
    ):

        fingerprint = identity.generate(
            content
        )


        return TrustDecision(
            component=identity.name,
            trusted=bool(fingerprint),
            score=1.0 if fingerprint else 0.0,
        )
