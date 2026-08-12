from dataclasses import dataclass
from typing import Dict, List, Optional

from ..provenance import ProvenanceEngine
from ..context_envelope import ContextEnvelopeStore


@dataclass
class Artifact:

    artifact_id: str
    artifact_type: str
    name: str
    source: str
    project_id: str
    metadata: Optional[dict] = None
    idea_id: Optional[str] = None


    @property
    def filename(self):
        """
        Backward compatibility
        with legacy code registry.
        """
        return self.name


    @property
    def language(self):
        """
        Backward compatibility
        with legacy code registry.
        """
        if self.metadata:
            return self.metadata.get("language")

        return None



class ArtifactRegistry:
    """
    First production wiring point for Article II (provenance) and Article
    XV.A (context envelope) -- both unratified/partially-unratified, see
    provenance/status.py and context_envelope/envelope.py. Both engines
    are optional and default to None: existing callers that construct
    ArtifactRegistry() with no arguments are unaffected.

    Context envelope registration is unconditional -- an empty envelope
    makes no claim, so there is nothing to get wrong by creating one.

    Provenance registration only happens if the caller passes an explicit
    provenance_status to register(). ProvenanceEngine.register() requires
    a status with no default by design (status.py: "must not guess
    provenance"); this wiring does not create a default it isn't entitled
    to. An artifact registered without a status simply has no provenance
    record yet, which is an honest absence, not a guess.
    """


    def __init__(
        self,
        provenance_engine: Optional[ProvenanceEngine] = None,
        context_envelope_store: Optional[ContextEnvelopeStore] = None,
    ):

        self.artifacts: Dict[str, Artifact] = {}
        self.counter = 0
        self.idea_links = {}
        self.provenance_engine = provenance_engine
        self.context_envelope_store = context_envelope_store



    def register(
        self,
        *args,
        **kwargs,
    ):

        """
        Supports:

        New:
            register(Artifact)
            register(Artifact, provenance_status=ProvenanceStatus.X)

        Legacy:
            register(filename, path, language)

        provenance_status is optional and keyword-only. See class
        docstring: no default is applied when it's omitted.
        """

        provenance_status = kwargs.pop(
            "provenance_status",
            None,
        )

        if (
            len(args) == 1
            and isinstance(args[0], Artifact)
        ):

            artifact = args[0]


        elif len(args) == 3:

            filename, path, language = args

            self.counter += 1

            artifact = Artifact(
                artifact_id=f"CODE-{self.counter:05d}",
                artifact_type="CODE",
                name=filename,
                source=path,
                project_id="UNKNOWN",
                metadata={
                    "language": language
                },
            )


        else:

            raise TypeError(
                "Invalid artifact registration format"
            )


        self.artifacts[
            artifact.artifact_id
        ] = artifact


        if self.context_envelope_store is not None:

            self.context_envelope_store.register(
                artifact.artifact_id
            )


        if (
            self.provenance_engine is not None
            and provenance_status is not None
        ):

            self.provenance_engine.register(
                artifact.artifact_id,
                provenance_status,
                source=artifact.source,
            )


        return artifact



    def get(
        self,
        artifact_id: str,
    ):

        return self.artifacts.get(
            artifact_id
        )



    def link_idea(
        self,
        artifact_id: str,
        idea_id: str,
    ):

        artifact = self.artifacts.get(
            artifact_id
        )

        if artifact:

            artifact.idea_id = idea_id


        if artifact_id not in self.idea_links:

            self.idea_links[artifact_id] = []


        self.idea_links[
            artifact_id
        ].append(
            idea_id
        )


        return True



    def ideas_for(
        self,
        artifact_id: str,
    ):

        return self.idea_links.get(
            artifact_id,
            [],
        )



    def search_by_project(
        self,
        project_id: str,
    ) -> List[Artifact]:

        return [
            artifact
            for artifact in self.artifacts.values()
            if artifact.project_id == project_id
        ]



    def list_all(self):

        return list(
            self.artifacts.values()
        )
