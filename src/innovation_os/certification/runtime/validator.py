class RuntimeValidator:


    def validate(
        self,
        report
    ):

        required = [
            "kernel",
            "governance",
            "memory",
            "agents",
            "learning",
        ]


        report.passed = all(
            item in report.checks
            for item in required
        )


        return report
