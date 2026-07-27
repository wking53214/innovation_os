import argparse

from src.innovation_os.config import CONFIG
from src.innovation_os.health.monitor import SystemHealth



def status():

    health = SystemHealth().check()

    return {
        "name": CONFIG.name,
        "version": CONFIG.version,
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
            f"{result['name']} {result['version']}"
        )

        print(
            "STATUS:",
            "HEALTHY"
            if result["healthy"]
            else "FAILED",
        )


if __name__ == "__main__":
    main()
