from innovation_os.intelligence.contracts import Evidence


class EvidenceEngine:
    name = "evidence_engine"

    def process(self, knowledge):

        return Evidence(
            source="knowledge_engine",
            evidence_type="derived",
            content=knowledge,
        )
