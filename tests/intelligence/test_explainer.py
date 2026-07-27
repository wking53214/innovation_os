from src.innovation_os.intelligence.explainer import (
    InnovationExplainer,
)



class FakeMemory:


    artifacts = [
        "governance.py"
    ]

    history = [
        "created"
    ]

    decisions = [
        "fail closed"
    ]

    provenance = [
        "design.md"
    ]


    def query(
        self,
        value,
    ):

        return self



def test_explain_idea():

    explainer = InnovationExplainer(
        FakeMemory(),
        None,
    )


    result = explainer.explain(
        "Sentinel"
    )


    assert (
        result.query
        ==
        "Sentinel"
    )


    assert (
        "governance.py"
        in
        result.artifacts
    )


    assert (
        "fail closed"
        in
        result.decisions
    )
