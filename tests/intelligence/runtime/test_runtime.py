from innovation_os.intelligence.bootstrap import (
    create_intelligence_kernel,
)

from innovation_os.intelligence.runtime import (
    IntelligenceRuntime,
)


def test_runtime_execution():

    kernel = create_intelligence_kernel()

    runtime = IntelligenceRuntime(
        kernel
    )

    artifact = runtime.execute(
        {
            "event": "test"
        }
    )

    assert artifact.intelligence_type == "inference"
    assert artifact.validate()
