from src.innovation_os.attribution.engine import (
    CodeAttributionEngine,
)


def test_code_attribution():

    engine = CodeAttributionEngine()


    engine.register_project(
        "PROJECT-SENTINEL",
        [
            "governance",
            "audit",
            "policy",
        ],
    )


    results = engine.attribute(
        "CODE-001",
        """
        governance engine
        audit ledger
        policy validation
        """,
    )


    assert len(results) == 1
    assert (
        results[0].project_id
        ==
        "PROJECT-SENTINEL"
    )

    assert results[0].confidence == 100.0



def test_no_match():

    engine = CodeAttributionEngine()


    engine.register_project(
        "PROJECT-001",
        [
            "biology",
        ],
    )


    results = engine.attribute(
        "CODE-002",
        "database service",
    )


    assert len(results) == 0
