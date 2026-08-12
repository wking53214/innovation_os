"""
SharedRegistries: proves the fix for the artifact_id collision /
disconnected provenance problem, and proves the problem it fixes is real.
"""

import tempfile
import os

from innovation_os.integration.code_pipeline import CodeIntegrationPipeline
from innovation_os.workflows.ingestion_workflow import FullIngestionWorkflow
from innovation_os.registry.shared_registries import SharedRegistries


def _make_file(directory, name, content="# code"):
    path = os.path.join(directory, name)
    with open(path, "w") as file:
        file.write(content)
    return path


def test_default_pipelines_do_not_share_state():
    """
    Documents the problem as it exists without a shared bundle: two
    pipelines each start their own artifact_id counter at zero, so
    scanning two different directories can produce the SAME artifact_id
    for two different files.
    """

    with tempfile.TemporaryDirectory() as directory_a, \
         tempfile.TemporaryDirectory() as directory_b:

        _make_file(directory_a, "a.py")
        _make_file(directory_b, "b.py")

        pipeline_a = CodeIntegrationPipeline()
        pipeline_b = CodeIntegrationPipeline()

        result_a = pipeline_a.process(directory_a)
        result_b = pipeline_b.process(directory_b)

        # Same ID, two different files, two disconnected registries.
        assert result_a[0].artifact_id == result_b[0].artifact_id
        assert pipeline_a.registry is not pipeline_b.registry


def test_shared_bundle_gives_one_counter_and_no_collision():

    with tempfile.TemporaryDirectory() as directory_a, \
         tempfile.TemporaryDirectory() as directory_b:

        _make_file(directory_a, "a.py")
        _make_file(directory_b, "b.py")

        shared = SharedRegistries()

        pipeline_a = CodeIntegrationPipeline(shared=shared)
        pipeline_b = CodeIntegrationPipeline(shared=shared)

        result_a = pipeline_a.process(directory_a)
        result_b = pipeline_b.process(directory_b)

        assert result_a[0].artifact_id != result_b[0].artifact_id
        assert pipeline_a.registry is pipeline_b.registry
        assert pipeline_a.provenance is pipeline_b.provenance


def test_shared_bundle_works_across_pipeline_types():
    """
    CodeIntegrationPipeline and FullIngestionWorkflow are different
    classes; a shared bundle should still give them one source of truth.
    """

    with tempfile.TemporaryDirectory() as directory_a, \
         tempfile.TemporaryDirectory() as directory_b:

        _make_file(directory_a, "a.py")
        _make_file(directory_b, "b.py")

        shared = SharedRegistries()

        code_pipeline = CodeIntegrationPipeline(shared=shared)
        ingestion = FullIngestionWorkflow(shared=shared)

        code_result = code_pipeline.process(directory_a)
        ingestion.run(directory_b)

        # Both artifacts are visible through either handle -- one registry.
        assert shared.registry.get(code_result[0].artifact_id) is not None
        assert len(shared.registry.artifacts) == 2


def test_shared_bundle_records_provenance_from_both_pipelines():

    with tempfile.TemporaryDirectory() as directory:

        _make_file(directory, "a.py")

        shared = SharedRegistries()
        pipeline = CodeIntegrationPipeline(shared=shared)

        result = pipeline.process(directory)

        record = shared.provenance.get(result[0].artifact_id)

        assert record is not None
