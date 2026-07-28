class AgentMessageRouter:


    def __init__(
        self,
        bus
    ):

        self.bus = bus



    def send(
        self,
        sender,
        receiver,
        message_type,
        payload
    ):

        from innovation_os.agents.communication import AgentMessage


        message = AgentMessage(
            sender=sender,
            receiver=receiver,
            message_type=message_type,
            payload=payload,
        )


        return self.bus.publish(
            message
        )
