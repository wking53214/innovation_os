import ast
from dataclasses import dataclass, field
from pathlib import Path
from typing import List



@dataclass
class CodeRelationship:

    source: str
    target: str
    relationship_type: str



@dataclass
class CodeAnalysis:

    file: str
    imports: List[str] = field(
        default_factory=list
    )
    relationships: List[CodeRelationship] = field(
        default_factory=list
    )



class CodeRelationshipExtractor:


    def analyze(
        self,
        file_path: str,
    ):

        path = Path(file_path)

        source = path.read_text()


        tree = ast.parse(
            source
        )


        imports = []

        relationships = []


        for node in ast.walk(tree):

            if isinstance(
                node,
                ast.Import,
            ):

                for item in node.names:

                    imports.append(
                        item.name
                    )

                    relationships.append(
                        CodeRelationship(
                            source=path.name,
                            target=item.name,
                            relationship_type="IMPORT",
                        )
                    )


            elif isinstance(
                node,
                ast.ImportFrom,
            ):

                if node.module:

                    imports.append(
                        node.module
                    )

                    relationships.append(
                        CodeRelationship(
                            source=path.name,
                            target=node.module,
                            relationship_type="IMPORT",
                        )
                    )


        return CodeAnalysis(
            file=path.name,
            imports=imports,
            relationships=relationships,
        )
