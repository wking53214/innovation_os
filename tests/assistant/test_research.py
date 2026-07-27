from src.innovation_os.assistant.research import (
    ResearchAssistant,
)


def test_research_assistant():

    assistant = ResearchAssistant()

    assistant.add_knowledge(
        "Sentinel OS AI governance platform"
    )

    assistant.add_knowledge(
        "Database optimization project"
    )


    answer = assistant.answer(
        "AI governance"
    )


    assert len(answer.matches) == 1
    assert "Sentinel" in answer.matches[0]
    assert answer.confidence > 0


def test_no_results():

    assistant = ResearchAssistant()

    assistant.add_knowledge(
        "biology research"
    )

    answer = assistant.answer(
        "quantum computing"
    )

    assert len(answer.matches) == 0
    assert answer.confidence == 0
