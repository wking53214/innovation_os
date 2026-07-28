from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class AgentTrustProfile:


    agent_id: str


    capability_scores: dict = field(
        default_factory=dict
    )


    governance_score: float = 0.0


    execution_count: int = 0


    last_updated: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )


    def overall_score(
        self
    ):

        capability_average = 0.0

        if self.capability_scores:

            capability_average = (
                sum(
                    self.capability_scores.values()
                )
                /
                len(
                    self.capability_scores
                )
            )


        return (
            capability_average * 0.7
            +
            self.governance_score * 0.3
        )
