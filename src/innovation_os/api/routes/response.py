from dataclasses import dataclass


@dataclass
class GatewayResponse:

    success: bool

    data: object

    message: str = ""
