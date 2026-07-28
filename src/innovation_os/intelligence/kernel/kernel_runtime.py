from .cognitive_kernel import CognitiveKernel


class IntelligenceKernel(CognitiveKernel):
    """
    Intelligence runtime kernel compatibility facade.
    """


    def register(
        self,
        name,
        component
    ):

        if hasattr(
            self.registry,
            "engines"
        ):
            self.registry.engines[name] = component

        else:
            self.state[name] = component



    def resolve(
        self,
        name
    ):

        if hasattr(
            self.registry,
            "engines"
        ):

            return self.registry.engines.get(
                name
            )

        return self.state.get(
            name
        )



    def list_components(self):

        if hasattr(
            self.registry,
            "engines"
        ):

            return list(
                self.registry.engines.keys()
            )

        return list(
            self.state.keys()
        )



    def health(self):

        return {
            "status": "ready",
            "components": len(
                self.list_components()
            ),
        }
