from dataclasses import dataclass, field
import uuid



@dataclass
class AgentTask:


    task_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )


    objective: str = ""

    required_capabilities: list = field(
        default_factory=list
    )


    assigned_agent: str = None


    status: str = "pending"
