import unittest
from dredge.bio_kernel import (
    PureThermodynamicsEngine, PureBiochemistryProteinEngine, BigDataGenomicsEngine,
    FastqQualityFilterEngine, PopulationGeneticsEngine, RNASecondaryStructureEngine,
    EnzymeInhibitionEngine
)

class TestScientificFramework(unittest.TestCase):
    def test_hardy_weinberg(self):
        # AA=49, Aa=42, aa=9 => p=0.7, q=0.3
        res = PopulationGeneticsEngine.calculate_hardy_weinberg(49, 42, 9)
        self.assertAlmostEqual(res['allele_frequency_p'], 0.7, places=2)
        self.assertEqual(res['equilibrium_status'], "IN_HARDY_WEINBERG_EQUILIBRIUM")

    def test_nussinov_rna(self):
        res = RNASecondaryStructureEngine.nussinov_fold("GGGAAACCC")
        self.assertTrue(res['max_nested_base_pairs'] >= 2)

    def test_enzyme_inhibition(self):
        # Competitive inhibition increases apparent Km while Vmax stays constant
        res = EnzymeInhibitionEngine.calculate_inhibition(v_max=100.0, k_m=10.0, inhibitor_conc=5.0, k_i=5.0, mode="competitive")
        self.assertEqual(res['apparent_Vmax'], 100.0)
        self.assertEqual(res['apparent_Km'], 20.0)

    def test_dna_tm(self):
        res = PureThermodynamicsEngine.calculate_melting_temp("GCGAATTCGC")
        self.assertIn('melting_temperature_Tm', res)

if __name__ == '__main__':
    unittest.main()
