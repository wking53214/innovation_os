from innovation_os.cli.mvp import (
    InnovationOS,
)



def test_mvp_status():

    system = InnovationOS()


    result = system.status()


    assert result["status"] == "READY"
    assert "Registry" in result["components"]
