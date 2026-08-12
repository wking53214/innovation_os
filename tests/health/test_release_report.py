from innovation_os.health.release_report import (
    ReleaseHealth,
)



def test_release_report():

    report = ReleaseHealth().generate(
        tests=180,
        modules=25,
    )


    assert (
        report.status
        ==
        "READY"
    )


    assert (
        report.tests
        ==
        180
    )
