from dataclasses import dataclass, field


@dataclass
class ArchitectureMap:

    modules: list = field(
        default_factory=list
    )


    def add_module(
        self,
        module
    ):

        self.modules.append(
            module
        )


    def find(
        self,
        name
    ):

        for module in self.modules:

            if module.name == name:
                return module

        return None
