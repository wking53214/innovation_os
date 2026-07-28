from innovation_os.intelligence.system.intelligence_system import (
    IntelligenceSystem,
)

from innovation_os.intelligence.runtime import (
    IntelligenceRuntime,
)

from innovation_os.intelligence.bootstrap import (
    create_intelligence_kernel,
)


def create_intelligence_system():

    kernel = create_intelligence_kernel()

    runtime = IntelligenceRuntime(
        kernel
    )

    return IntelligenceSystem(
        runtime=runtime
    )
