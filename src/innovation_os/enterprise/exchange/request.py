from dataclasses import dataclass
import uuid


@dataclass
class DataExchangeRequest:


    source_system: str

    payload: dict

    request_id: str = uuid.uuid4().hex
