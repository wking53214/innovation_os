from innovation_os.code_registry.engine import (
    CodeRegistryEngine,
)


def test_register_artifact():

    engine = CodeRegistryEngine()

    artifact = engine.register_artifact(
        artifact_id="CODE-0001",
        file_name="solution.py",
        path="/projects/test/solution.py",
        idea_id="IDEA-0001",
        problem_id="PROBLEM-0001",
        language="Python",
        purpose="Prototype solution engine",
        tags=[
            "prototype",
        ],
    )

    assert artifact.artifact_id == "CODE-0001"
    assert artifact.language == "Python"


def test_get_artifact():

    engine = CodeRegistryEngine()

    engine.register_artifact(
        artifact_id="CODE-0002",
        file_name="engine.py",
        path="/src/engine.py",
        idea_id="IDEA-0002",
        problem_id="PROBLEM-0002",
        language="Python",
        purpose="Core logic",
    )

    artifact = engine.get_artifact(
        "CODE-0002"
    )

    assert artifact.artifact_id == "CODE-0002"
    assert artifact.file_name == "engine.py"
    assert artifact.idea_id == "IDEA-0002"


def test_find_by_idea():

    engine = CodeRegistryEngine()

    engine.register_artifact(
        artifact_id="CODE-0003",
        file_name="test.py",
        path="/test.py",
        idea_id="IDEA-0003",
        problem_id="PROBLEM-0003",
        language="Python",
        purpose="Testing",
    )

    results = engine.find_by_idea(
        "IDEA-0003"
    )

    assert len(results) == 1
