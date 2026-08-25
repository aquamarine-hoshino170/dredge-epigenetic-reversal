"""
DREDGE: High-Performance Computational Biophysics & Genomic Framework
"""

__version__ = "47.0.0"

from dredge.bio_kernel import (
    PureThermodynamicsEngine,
    PureBiochemistryProteinEngine,
    PureMolecularGenomicsEngine
)

__all__ = [
    "PureThermodynamicsEngine",
    "PureBiochemistryProteinEngine",
    "PureMolecularGenomicsEngine"
]
