class ExchangePolicy:


    def __init__(
        self,
        allowed_sources=None
    ):

        self.allowed_sources = (
            allowed_sources
            or []
        )



    def allowed(
        self,
        source
    ):

        return (
            source
            in
            self.allowed_sources
        )
