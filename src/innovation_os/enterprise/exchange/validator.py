class DataValidator:


    def validate(
        self,
        request
    ):

        if not request.payload:

            return False


        return True
