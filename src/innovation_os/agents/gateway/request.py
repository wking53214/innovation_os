from dataclasses import dataclass


@dataclass
class AgentExecutionRequest:


    agent_id: str

    capability: str

    payload: dict
