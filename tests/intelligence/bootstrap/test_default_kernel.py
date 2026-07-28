from innovation_os.intelligence.bootstrap import (
    create_intelligence_kernel,
)


def test_default_kernel_creation():

    kernel = create_intelligence_kernel()

    assert "observation" in kernel.registry.engines
    assert "inference" in kernel.registry.engines

    assert "pattern" in kernel.registry.adapters

    assert "signal" in kernel.registry.contracts
