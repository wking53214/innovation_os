from pathlib import Path


class RepositoryConnector:


    def __init__(
        self,
        path
    ):

        self.path = Path(
            path
        )


    def connect(self):

        return self.path.exists()


    def collect(self):

        if not self.connect():

            return []


        files = []


        for item in self.path.rglob("*"):

            if item.is_file():

                files.append(
                    {
                        "file": str(item),
                        "extension": item.suffix,
                    }
                )


        return files
