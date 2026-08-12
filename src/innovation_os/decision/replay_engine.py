from typing import List, Optional

from innovation_os.decision.replay import DecisionReplay


class ReplayEngine:

    def __init__(self):
        self.replays: List[DecisionReplay] = []

    def create_replay(
        self,
        decision_id: str,
        original_choice: str,
        original_assumptions: List[str],
        new_information: List[str],
        reconsidered_options: List[str],
        conclusion: str,
    ) -> DecisionReplay:

        replay = DecisionReplay(
            decision_id=decision_id,
            original_choice=original_choice,
            original_assumptions=original_assumptions,
            new_information=new_information,
            reconsidered_options=reconsidered_options,
            conclusion=conclusion,
        )

        self.replays.append(replay)

        return replay

    def get_replay(
        self,
        decision_id: str,
    ) -> Optional[DecisionReplay]:

        for replay in self.replays:
            if replay.decision_id == decision_id:
                return replay

        return None
