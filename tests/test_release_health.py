from innovation_os.health import (
    SystemHealth,
)


def test_release_health():

    result = SystemHealth().check()

    assert result.healthy is True
    assert result.version == "1.0.0"
    assert len(result.components) > 0
