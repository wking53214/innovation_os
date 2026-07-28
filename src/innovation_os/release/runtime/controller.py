from innovation_os.release import (
    ReleaseManifest,
)


class ReleaseController:


    def build_manifest(
        self,
        version,
        components
    ):

        return ReleaseManifest(
            version=version,
            components=components,
            certified=True,
        )
