class ContextEngine:
    name = "context_engine"

    def process(self, perception):

        return {
            "context": perception,
            "relationships": [],
        }
