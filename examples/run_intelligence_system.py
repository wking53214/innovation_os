from innovation_os.application import IntelligenceSystem


def main():

    system = IntelligenceSystem()


    result = system.execute(
        key="demo_analysis",
        payload={
            "repository": "innovation_os",
            "operation": "architecture_analysis",
        },
        objective="identify system capabilities",
    )


    print("=" * 60)
    print("INTELLIGENCE SYSTEM RESULT")
    print("=" * 60)

    print(result)

    print("\nEVENT HISTORY")

    for event in system.logger.history():
        print(event)



if __name__ == "__main__":
    main()
