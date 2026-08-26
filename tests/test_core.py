import unittest
from dredge.physics import QuantumCore, SignalCore, OrbitalCore
from dredge.biology import BiologyCore
from dredge.chemistry import ChemistryCore
from dredge.math_crypto import MathCore, CryptoCore

class TestRealCore(unittest.TestCase):
    def test_quantum(self):
        res = QuantumCore.simulate_bell_pair()
        self.assertEqual(res['|00>'], 0.5)
        self.assertEqual(res['|11>'], 0.5)

    def test_orbital(self):
        res = OrbitalCore.step_orbit(steps=10)
        self.assertTrue(res['final_radius'] > 0.0)

    def test_biology_thermo(self):
        res = BiologyCore.dna_thermodynamics("GCATGCATGC")
        self.assertTrue(res['Tm_C'] > 0.0)

    def test_chemistry_kinetics(self):
        res = ChemistryCore.arrhenius_rate(temp_c=25.0, ea_kj=50.0)
        self.assertIn("s⁻¹", res['rate_constant_k'])

    def test_math_curvature(self):
        res = MathCore.riemann_ricci_curvature()
        self.assertTrue(res['determinant'] > 0.0)

    def test_crypto_pedersen(self):
        res = CryptoCore.verify_ledger([100, 200, 300])
        self.assertTrue(res['verified'])

if __name__ == '__main__':
    unittest.main()
