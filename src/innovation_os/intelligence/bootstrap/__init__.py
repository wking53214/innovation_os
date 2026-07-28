from innovation_os.intelligence.system import (
    create_intelligence_system,
)

from innovation_os.intelligence.kernel import (
    create_kernel,
)



def create_intelligence_kernel():

    kernel = create_kernel()


    defaults = [
        "observation",
        "perception",
        "context",
        "knowledge",
        "inference",
        "hypothesis",
    ]


    for engine in defaults:

        kernel.register(
            engine,
            None
        )


    adapters = [
        "pattern",
        "repository",
        "cluster",
        "duplicate",
        "knowledge_graph",
    ]


    for adapter in adapters:

        kernel.registry.adapters[adapter] = None


    contracts = [
        "signal",
        "observation",
        "perception",
        "context",
        "knowledge",
        "evidence",
        "confidence",
        "hypothesis",
        "inference",
        "intelligence_artifact",
    ]


    for contract in contracts:

        kernel.registry.contracts[contract] = None


    
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

return kernel




def bootstrap_intelligence(
    pipeline
):

    kernel = create_intelligence_kernel()


    system = create_intelligence_system(
        pipeline
    )


    kernel.register(
        "intelligence_system",
        system
    )


    
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

return kernel




__all__ = [
    "bootstrap_intelligence",
    "create_intelligence_kernel",
]
