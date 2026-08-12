from innovation_os.audit.architecture_audit import (
    ArchitectureAudit,
)



def test_architecture_scan():

    audit = ArchitectureAudit()

    result = audit.summary()

    assert result["modules"] > 0
    assert result["files"] > 0
