from innovation_os.reconstruction.project_reconstruction import (
    ProjectReconstructionEngine,
)



def test_project_reconstruction():

    engine = ProjectReconstructionEngine()


    result = engine.reconstruct(
        "PROJECT-001",
        [
            "gsa_gateway.py",
            "audit_ledger.py",
        ],
        [
            "AI",
            "governance",
        ],
    )


    assert result.project_id == "PROJECT-001"
    assert len(result.artifacts) == 2
    assert result.confidence == 100
