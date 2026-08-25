"""
DREDGE: High-Performance Computational Biophysics & Analytical Chemistry Framework
"""

__version__ = "48.0.0"

from dredge.bio_kernel import (
    PureThermodynamicsEngine,
    PureBiochemistryProteinEngine,
    PureMolecularGenomicsEngine,
    PureEnzymeKineticsEngine,
    PureBufferEquilibriumEngine,
    PureSpectrophotometryEngine
)

__all__ = [
    "PureThermodynamicsEngine",
    "PureBiochemistryProteinEngine",
    "PureMolecularGenomicsEngine",
    "PureEnzymeKineticsEngine",
    "PureBufferEquilibriumEngine",
    "PureSpectrophotometryEngine"
]
