from dataclasses import dataclass


@dataclass
class AgentExecutionDecision:


    approved: bool

    reason: str

    agent_id: str

    capability: str
