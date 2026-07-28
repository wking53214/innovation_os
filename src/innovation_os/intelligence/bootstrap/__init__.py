from innovation_os.intelligence.system import (
    create_intelligence_system,
)

from innovation_os.intelligence.kernel import (
    create_kernel,
)





def create_intelligence_kernel():

    from innovation_os.intelligence.kernel import (
        IntelligenceKernel
    )

    kernel = IntelligenceKernel()

    kernel.registry.engines.update(
        {
            "observation": None,
            "perception": None,
            "context": None,
            "knowledge": None,
            "inference": None,
            "hypothesis": None,
        }
    )

    kernel.registry.adapters.update(
        {
            "pattern": None,
            "repository": None,
            "cluster": None,
            "duplicate": None,
            "knowledge_graph": None,
        }
    )

    kernel.registry.contracts.update(
        {
            "signal": None,
            "observation": None,
            "perception": None,
            "context": None,
            "knowledge": None,
            "evidence": None,
            "confidence": None,
            "hypothesis": None,
            "inference": None,
            "intelligence_artifact": None,
        }
    )

    return kernel





def bootstrap_intelligence(
    pipeline
):

    from innovation_os.intelligence.system import (
        create_intelligence_system
    )

    kernel = create_intelligence_kernel()

    system = create_intelligence_system(
        pipeline
    )

    kernel.register(
        "intelligence_system",
        system
    )

    return kernel

