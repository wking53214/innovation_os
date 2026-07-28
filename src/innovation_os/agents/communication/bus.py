class AgentMessageBus:


    def __init__(self):

        self.messages = []


    def send(
        self,
        message
    ):

        self.messages.append(
            message
        )


    def inbox(
        self,
        agent
    ):

        return [
            m for m in self.messages
            if m.receiver == agent
        ]
