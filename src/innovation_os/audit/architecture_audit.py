from dataclasses import dataclass
from pathlib import Path



@dataclass
class ModuleReport:

    module: str
    files: int



class ArchitectureAudit:


    def scan(
        self,
        root="src/innovation_os",
    ):

        reports = []

        path = Path(root)


        for item in sorted(path.iterdir()):

            if item.is_dir():

                files = len(
                    list(
                        item.rglob("*.py")
                    )
                )

                reports.append(
                    ModuleReport(
                        item.name,
                        files,
                    )
                )


        return reports



    def summary(
        self,
        root="src/innovation_os",
    ):

        reports = self.scan(root)

        return {
            "modules": len(reports),
            "files": sum(
                r.files
                for r in reports
            ),
        }
