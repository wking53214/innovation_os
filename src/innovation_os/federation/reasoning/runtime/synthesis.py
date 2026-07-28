class ReasoningSynthesisEngine:


    def synthesize(
        self,
        results
    ):


        if not results:

            return {
                "conclusion":
                None,

                "confidence":
                0.0
            }



        confidence = round(
            sum(
                item.confidence
                for item in results
            ) / len(results),
            2
        )



        conclusions = [
            item.conclusion
            for item
            in results
        ]



        consensus = (
            len(set(conclusions))
            ==
            1
        )



        return {

            "conclusion":
            conclusions[0]
            if consensus
            else "conflict_detected",

            "confidence":
            confidence,

            "consensus":
            consensus

        }
