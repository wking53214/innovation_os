class DependencyAnalyzer:


    def analyze(
        self,
        module
    ):

        return {
            "module": module.name,
            "dependencies": module.dependencies,
            "count": len(module.dependencies),
        }
