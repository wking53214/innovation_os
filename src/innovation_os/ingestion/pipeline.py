from .importer import FileImporter
from .normalizer import ArtifactNormalizer



class IngestionPipeline:


    def __init__(self):

        self.importer = FileImporter()
        self.normalizer = ArtifactNormalizer()



    def ingest(
        self,
        directory,
    ):

        files = self.importer.scan(
            directory
        )


        return [
            self.normalizer.normalize(
                file
            )
            for file in files
        ]
