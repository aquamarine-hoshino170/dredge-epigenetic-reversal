import unittest
from dredge.bio_kernel import (
    PureThermodynamicsEngine,
    PureBiochemistryProteinEngine,
    PureMolecularGenomicsEngine,
    PureEnzymeKineticsEngine,
    PureBufferEquilibriumEngine,
    PureSpectrophotometryEngine
)

class TestPureBiophysicsKernel(unittest.TestCase):
    def test_dna_melting_temp(self):
        res = PureThermodynamicsEngine.calculate_melting_temp("GCGAATTCGC")
        self.assertIn("melting_temperature_Tm", res)

    def test_protein_isoelectric_point(self):
        res = PureBiochemistryProteinEngine.calculate_isoelectric_point("DDDDDD")
        self.assertTrue(res["isoelectric_point_pI"] < 4.0)

    def test_ribosomal_translation(self):
        self.assertEqual(PureMolecularGenomicsEngine.translate("ATGGCTTAA"), "MA*")

    def test_enzyme_kinetics_lineweaver(self):
        s = [5.0, 10.0, 20.0, 40.0]
        v = [(100.0 * x) / (10.0 + x) for x in s]
        res = PureEnzymeKineticsEngine.fit_lineweaver_burk(s, v)
        self.assertAlmostEqual(res["v_max"], 100.0, places=2)

    def test_buffer_ph(self):
        res = PureBufferEquilibriumEngine.calculate_buffer_ph(4.76, 0.1, 0.1)
        self.assertAlmostEqual(res["equilibrium_ph"], 4.76, places=2)

    def test_spectrophotometry(self):
        res = PureSpectrophotometryEngine.quantify_nucleic_acid(1.0, 0.53)
        self.assertEqual(res["concentration_ng_ul"], 50.0)

if __name__ == "__main__":
    unittest.main()
