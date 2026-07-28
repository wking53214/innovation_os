from dataclasses import dataclass


@dataclass
class RepositoryIntelligenceEngine:

    architecture_map: object

    fingerprint_engine: object


    def analyze(
        self,
        modules
    ):

        results = []

        for module in modules:

            self.architecture_map.add_module(
                module
            )

            results.append(
                self.fingerprint_engine.generate(
                    module
                )
            )

        return results
