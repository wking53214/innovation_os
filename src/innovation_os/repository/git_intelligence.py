from dataclasses import dataclass
from typing import List
import subprocess



@dataclass
class GitCommit:

    commit_id: str

    message: str

    files: List[str]



class GitIntelligence:


    def commits(
        self,
        directory: str,
    ):

        result = subprocess.run(
            [
                "git",
                "-C",
                directory,
                "log",
                "--format=%H|%s",
                "--name-only",
            ],
            capture_output=True,
            text=True,
        )


        commits = []

        current = None


        for line in result.stdout.splitlines():

            if "|" in line:

                parts = line.split(
                    "|",
                    1,
                )

                current = GitCommit(
                    commit_id=parts[0],
                    message=parts[1],
                    files=[],
                )

                commits.append(
                    current
                )


            elif line.strip() and current:

                current.files.append(
                    line.strip()
                )


        return commits



    def files_changed(
        self,
        directory: str,
    ):

        results = []


        for commit in self.commits(
            directory
        ):

            results.extend(
                commit.files
            )


        return results
