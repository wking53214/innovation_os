from innovation_os.intelligence.contracts import (
    Signal,
    Observation,
)


class ObservationEngine:
    name = "observation_engine"

    def process(self, signal: Signal):

        return Observation(
            source=signal.source,
            subject=signal.signal_type,
            data=signal.payload,
            confidence=0.5,
        )
