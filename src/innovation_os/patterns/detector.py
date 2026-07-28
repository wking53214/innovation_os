class PatternDetector:


    def detect(
        self,
        data,
    ):

        patterns = []

        if isinstance(
            data,
            dict
        ):

            keys = list(
                data.keys()
            )

            if keys:

                patterns.append(
                    {
                        "type": "structure",
                        "keys": keys,
                    }
                )


        return patterns
