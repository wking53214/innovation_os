from innovation_os.interface.cli import (
    InnovationInterface,
)


def test_status_view():

    interface = InnovationInterface()

    result = interface.status(
        100,
        5,
        20,
    )


    assert result.title == (
        "Innovation OS Status"
    )

    assert (
        "Artifacts: 100"
        in result.sections
    )



def test_summary():

    interface = InnovationInterface()

    result = interface.summarize(
        "Projects",
        [
            "Sentinel OS",
        ],
    )


    assert result.sections[0] == (
        "Sentinel OS"
    )
