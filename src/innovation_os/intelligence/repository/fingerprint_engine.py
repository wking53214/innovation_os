from dataclasses import dataclass


@dataclass
class SystemFingerprint:

    identity: str

    signature: dict



class FingerprintEngine:


    def generate(
        self,
        module
    ):

        return SystemFingerprint(
            identity=module.name,
            signature={
                "path": module.path,
                "dependencies": module.dependencies,
                "consumer_count": len(module.consumers),
            }
        )
