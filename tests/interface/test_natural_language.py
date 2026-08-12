from innovation_os.interface.natural_language import (
    NaturalLanguageInterface,
)



def test_question_detection():

    interface = NaturalLanguageInterface()


    interface.add(
        "PROJECT-SENTINEL",
        "AI governance security platform",
    )


    result = interface.query(
        "What projects involve AI governance?"
    )


    assert result.intent == "SEARCH"
    assert "PROJECT-SENTINEL" in result.matches



def test_recommendation_intent():

    interface = NaturalLanguageInterface()


    result = interface.query(
        "What should I work on next?"
    )


    assert result.intent == "RECOMMEND"
