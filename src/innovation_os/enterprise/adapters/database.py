from .base import EnterpriseAdapter



class DatabaseAdapter(
    EnterpriseAdapter
):


    source_system = "database"



    def normalize(
        self,
        payload
    ):

        return {

            "records":
            payload.get(
                "records",
                []
            ),

            "schema":
            payload.get(
                "schema",
                {}
            )

        }
