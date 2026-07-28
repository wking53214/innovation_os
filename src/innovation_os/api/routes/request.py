from dataclasses import dataclass


@dataclass
class GatewayRequest:

    token: str

    operation: str

    payload: dict
