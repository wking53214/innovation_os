# The telemetry subsystem used to keep its own copy of IntelligenceMetrics.
# It now re-exports the canonical implementation from the metrics package
# so there is a single source of truth for this class.
from innovation_os.intelligence.metrics.intelligence_metrics import (
    IntelligenceMetrics,
)

__all__ = ["IntelligenceMetrics"]
