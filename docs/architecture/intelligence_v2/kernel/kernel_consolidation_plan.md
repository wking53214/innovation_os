# Intelligence V2 Kernel Consolidation Plan


## Target State

Single authoritative kernel boundary:

innovation_os.intelligence.kernel


## Required Exports

- IntelligenceKernel
- CognitiveKernel
- IntelligenceRegistry
- create_kernel
- create_intelligence_kernel


## Compatibility Requirements

Existing imports must continue working:

from innovation_os.intelligence.kernel import ...


## Consolidation Rules

1. Do not remove working contracts.
2. Do not duplicate registries.
3. Kernel owns lifecycle only.
4. Bootstrap creates configured instances.
5. Runtime executes through kernel-managed components.


## Validation

Before merge:

- kernel tests pass
- bootstrap tests pass
- system tests pass
- full intelligence suite passes
