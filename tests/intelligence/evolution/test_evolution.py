from innovation_os.intelligence.evolution import (
    KnowledgeGrowth,
    PatternEvolution,
    ConceptMapper,
)


def test_evolution():

    knowledge = KnowledgeGrowth()

    knowledge.add(
        "concept"
    )

    patterns = PatternEvolution()

    patterns.evolve(
        "pattern",
        "updated"
    )

    mapper = ConceptMapper()

    mapper.map(
        "AI",
        "reasoning"
    )

    assert knowledge.size() == 1
    assert patterns.patterns
    assert mapper.concepts
