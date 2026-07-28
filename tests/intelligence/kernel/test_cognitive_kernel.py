from innovation_os.intelligence.kernel import CognitiveKernel


class DemoEngine:

    def process(self, payload):
        return payload


def test_kernel_execution():

    kernel = CognitiveKernel()

    kernel.register_engine(
        "demo",
        DemoEngine()
    )

    result = kernel.execute(
        "demo",
        {"value": 1}
    )

    assert result["value"] == 1
