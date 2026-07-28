from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class StoredObject:

    key: str
    value: object
    created_at: datetime


class MemoryRepository:

    def __init__(self):

        self.storage = {}


    def save(
        self,
        key,
        value
    ):

        obj = StoredObject(
            key=key,
            value=value,
            created_at=datetime.now(
                timezone.utc
            ),
        )

        self.storage[key] = obj

        return obj


    def get(
        self,
        key
    ):

        item = self.storage.get(
            key
        )

        if item:
            return item.value

        return None


    def all(self):

        return list(
            self.storage.values()
        )
