from dataclasses import dataclass


@dataclass
class EntityResolver:
    """
    Finds matching knowledge entities.
    """


    def match(
        self,
        left,
        right
    ):

        return (
            left.name.lower()
            ==
            right.name.lower()
        )
