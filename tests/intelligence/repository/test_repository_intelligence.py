from innovation_os.intelligence.repository import (
    IntelligenceModule,
    ArchitectureMap,
    FingerprintEngine,
    RepositoryIntelligenceEngine,
)


def test_architecture_map():

    amap = ArchitectureMap()

    module = IntelligenceModule(
        "memory",
        "src/memory",
    )

    amap.add_module(
        module
    )

    assert amap.find("memory") == module



def test_fingerprint():

    engine = FingerprintEngine()

    module = IntelligenceModule(
        "reasoning",
        "src/reasoning",
        dependencies=[
            "knowledge"
        ]
    )

    fingerprint = engine.generate(
        module
    )

    assert fingerprint.identity == "reasoning"
    assert fingerprint.signature["dependencies"] == [
        "knowledge"
    ]



def test_repository_engine():

    engine = RepositoryIntelligenceEngine(
        ArchitectureMap(),
        FingerprintEngine(),
    )

    results = engine.analyze(
        [
            IntelligenceModule(
                "core",
                "src/core"
            )
        ]
    )

    assert len(results) == 1
