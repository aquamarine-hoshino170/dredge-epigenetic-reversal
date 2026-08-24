import pytest
from dredge.core import WaddingtonPotentialEngine

def test_waddington_engine_physics():
    engine = WaddingtonPotentialEngine(n_cpg_sites=1000)
    res = engine.simulate_tet2_reversal(steps=50, catalytic_rate=0.3)
    
    assert res['final_entropy_bits'] < res['initial_entropy_bits'], "Entropy must decrease under active TET2 modulation"
    assert 0.0 <= res['methylation_mean'] <= 1.0
    assert len(res['trajectory']) == 51
