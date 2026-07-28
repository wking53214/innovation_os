from dataclasses import dataclass, field


@dataclass
class IntelligenceFabric:

    nodes: dict = field(
        default_factory=dict
    )


    def register(
        self,
        name,
        component
    ):

        self.nodes[name] = component


    def resolve(
        self,
        name
    ):

        return self.nodes.get(
            name
        )


    def inventory(self):

        return list(
            self.nodes.keys()
        )
