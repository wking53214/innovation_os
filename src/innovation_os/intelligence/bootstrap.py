from innovation_os.intelligence.system import (
    create_intelligence_system,
)

from innovation_os.intelligence.kernel import (
    create_kernel,
)



def bootstrap_intelligence(
    pipeline
):

    kernel = create_kernel()

    system = create_intelligence_system(
        pipeline
    )


    kernel.register(
        "intelligence_system",
        system
    )


    return kernel
