from src.innovation_os.platform.health import (
    SystemHealth,
)

from src.innovation_os.platform.version import (
    VersionRegistry,
)



def test_health():

    health = SystemHealth()

    health.register(
        "graph",
        True,
        "available",
    )


    result = health.report()


    assert result["graph"] is True



def test_version():

    registry = VersionRegistry()


    registry.register(
        "CODE-001",
        "1.0",
        "ACTIVE",
    )


    result = registry.get(
        "CODE-001"
    )


    assert result[0].version == "1.0"
