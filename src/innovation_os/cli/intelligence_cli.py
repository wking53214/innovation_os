import json
import sys

from innovation_os.api import IntelligenceService


def main():

    service = IntelligenceService()

    payload = {
        "input": " ".join(sys.argv[1:])
    }

    result = service.analyze(
        payload=payload,
        objective="general analysis",
    )

    print(
        json.dumps(
            {
                "status": result.status,
                "confidence": result.confidence,
                "artifact": str(
                    result.artifact
                ),
            },
            indent=2,
            default=str,
        )
    )


if __name__ == "__main__":
    main()
