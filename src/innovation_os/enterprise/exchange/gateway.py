from .result import ExchangeResult
from .provenance import ProvenanceRecord



class GovernedDataExchangeGateway:


    def __init__(
        self,
        validator,
        policy
    ):

        self.validator = validator

        self.policy = policy

        self.provenance = []



    def process(
        self,
        request,
        adapter
    ):


        if not self.validator.validate(
            request
        ):

            return ExchangeResult(
                False,
                "validation_failed"
            )



        if not self.policy.allowed(
            request.source_system
        ):

            return ExchangeResult(
                False,
                "source_not_allowed"
            )



        artifact = adapter.ingest(
            request.payload
        )



        self.provenance.append(
            ProvenanceRecord(
                request.source_system,
                request.request_id
            )
        )



        return ExchangeResult(
            True,
            "approved",
            artifact
        )
