import argparse

from innovation_os.config import CONFIG
from innovation_os.health.monitor import SystemHealth



def status():

    health = SystemHealth().check()

    return {
        "environment": CONFIG.environment,
        "version": health.version,
        "healthy": health.healthy,
    }



def main():

    parser = argparse.ArgumentParser(
        prog="innovation-os"
    )

    parser.add_argument(
        "command",
        nargs="?",
        default="status",
    )

    args = parser.parse_args()

    if args.command == "status":

        result = status()

        print(
            f"innovation-os {result['version']} ({result['environment']})"
        )

        print(
            "STATUS:",
            "HEALTHY"
            if result["healthy"]
            else "FAILED",
        )


if __name__ == "__main__":
    main()
