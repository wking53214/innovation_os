from innovation_os.security import (
    AuthenticationService,
)

from .request import GatewayRequest
from .response import GatewayResponse


class APIGateway:


    def __init__(
        self,
        service=None
    ):

        self.auth = AuthenticationService()

        self.service = service


    def handle(
        self,
        request: GatewayRequest
    ):

        auth = self.auth.authenticate(
            request.token
        )

        if not auth.authenticated:

            return GatewayResponse(
                success=False,
                data=None,
                message="unauthorized",
            )


        if self.service:

            result = self.service.execute(
                request.operation,
                request.payload
            )

        else:

            result = {
                "operation":
                request.operation,
                "accepted":
                True,
            }


        return GatewayResponse(
            success=True,
            data=result,
            message="complete",
        )
