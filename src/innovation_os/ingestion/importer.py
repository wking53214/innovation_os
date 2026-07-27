from pathlib import Path



class FileImporter:


    def scan(
        self,
        directory: str,
    ):

        root = Path(directory)


        return [
            path
            for path in root.rglob("*")
            if path.is_file()
        ]
