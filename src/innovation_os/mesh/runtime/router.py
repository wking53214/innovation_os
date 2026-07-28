class MessageRouter:


    def route(
        self,
        message,
        registry
    ):

        target = registry.get(
            message.target
        )


        if target:

            return {
                "delivered": True,
                "target": target.name,
                "payload": message.payload,
            }


        return {
            "delivered": False
        }
