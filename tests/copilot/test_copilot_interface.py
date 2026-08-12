from innovation_os.copilot.interface import (
    InnovationCopilot,
)


def test_copilot_question():

    copilot = InnovationCopilot()

    copilot.add(
        "Sentinel AI governance platform"
    )


    response = copilot.ask(
        "AI governance"
    )


    assert len(response.findings) == 1
    assert "Sentinel" in response.findings[0]


def test_empty_response():

    copilot = InnovationCopilot()

    response = copilot.ask(
        "quantum biology"
    )


    assert len(response.findings) == 0
