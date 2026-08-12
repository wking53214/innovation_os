"""
One shared registry/provenance/context-envelope bundle.

Every ArtifactRegistry, ProvenanceEngine, and ContextEnvelopeStore built
independently is its own island: separate artifacts dict, separate
artifact_id counter, separate provenance history. Two pipelines that each
construct their own (the previous default for CodeIntegrationPipeline and
FullIngestionWorkflow) can even assign the SAME artifact_id to two
different files, since each counter starts at zero independently.

SharedRegistries is the fix: build one, pass it to every pipeline that
should agree on what "CODE-00001" refers to. Nothing forces its use --
each pipeline still defaults to a private, isolated set when no shared
bundle is given, which is what the existing tests rely on.
"""

from dataclasses import dataclass, field

from .artifact_registry import ArtifactRegistry
from ..provenance import ProvenanceEngine
from ..context_envelope import ContextEnvelopeStore


@dataclass
class SharedRegistries:

    provenance: ProvenanceEngine = field(
        default_factory=ProvenanceEngine
    )

    context_envelopes: ContextEnvelopeStore = field(
        default_factory=ContextEnvelopeStore
    )

    registry: ArtifactRegistry = field(
        init=False,
    )

    def __post_init__(self):

        self.registry = ArtifactRegistry(
            provenance_engine=self.provenance,
            context_envelope_store=self.context_envelopes,
        )
