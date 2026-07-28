from innovation_os.api import IntelligenceService
from innovation_os.memory import IntelligenceMemory


def main():

    memory = IntelligenceMemory()

    service = IntelligenceService()

    result = service.analyze(
        payload={
            "event": "repository_scan",
            "value": "innovation_os",
        },
        objective="understand system behavior",
    )

    memory.store(
        "first_analysis",
        result,
    )

    print(result)

    print(
        memory.retrieve(
            "first_analysis"
        )
    )


if __name__ == "__main__":
    main()
