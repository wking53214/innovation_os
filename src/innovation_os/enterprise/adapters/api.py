from .base import EnterpriseAdapter



class APIAdapter(
    EnterpriseAdapter
):


    source_system = "api"



    def normalize(
        self,
        payload
    ):

        return {

            "request":
            payload.get(
                "request"
            ),

            "response":
            payload.get(
                "response"
            )

        }
