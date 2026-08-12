from innovation_os.cli.main import (
    status,
)


def test_cli_status():

    result = status()

    assert result["healthy"] is True
    assert result["environment"] == "development"
    assert result["version"] == "1.0.0"
