class AgentMessageBus:


    def __init__(self):

        self.messages = []



    def publish(
        self,
        message
    ):

        self.messages.append(
            message
        )

        return message



    def inbox(
        self,
        agent_id
    ):

        return [

            message

            for message
            in self.messages

            if message.receiver
            ==
            agent_id

        ]



    def history(
        self
    ):

        return list(
            self.messages
        )
