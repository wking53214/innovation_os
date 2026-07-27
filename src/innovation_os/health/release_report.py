from dataclasses import dataclass
from datetime import datetime
import sys



@dataclass
class ReleaseReport:

    python_version: str

    generated_at: str

    status: str

    tests: int = 0

    modules: int = 0



class ReleaseHealth:


    def generate(
        self,
        tests=0,
        modules=0,
    ):

        return ReleaseReport(

            python_version=sys.version.split()[0],

            generated_at=datetime.now().isoformat(),

            status="READY",

            tests=tests,

            modules=modules,
        )
