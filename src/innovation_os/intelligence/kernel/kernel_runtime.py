from dataclasses import dataclass, field

from .intelligence_registry import IntelligenceRegistry


@dataclass
class IntelligenceKernel:

    registry: IntelligenceRegistry = field(
        default_factory=IntelligenceRegistry
    )

    state: dict = field(
        default_factory=dict
    )


    def register(
        self,
        name,
        component
    ):

        self.state[name] = component

        return component


    def resolve(
        self,
        name
    ):

        return self.state.get(name)


    def start(self):

        self.state["status"] = "running"

        return self


    def stop(self):

        self.state["status"] = "stopped"

        return self


    def status(self):

        return self.state.get(
            "status",
            "initialized"
        )



def create_kernel():

    return IntelligenceKernel()



def create_intelligence_kernel():

    return IntelligenceKernel()
