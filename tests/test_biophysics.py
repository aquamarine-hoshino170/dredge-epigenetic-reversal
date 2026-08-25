import unittest
from dredge.bio_kernel import (
    PureThermodynamicsEngine, PureBiochemistryProteinEngine, BigDataGenomicsEngine,
    FastqQualityFilterEngine, PopulationGeneticsEngine, RNASecondaryStructureEngine,
    EnzymeInhibitionEngine, PhylogeneticTreeEngine, GeneticLinkageMappingEngine,
    AllostericCooperativityEngine
)

class TestScientificFramework(unittest.TestCase):
    def test_upgma_phylogenetics(self):
        taxa = ["A", "B", "C"]
        mat = [[0.0, 2.0, 4.0], [2.0, 0.0, 4.0], [4.0, 4.0, 0.0]]
        res = PhylogeneticTreeEngine.construct_upgma_tree(taxa, mat)
        self.assertTrue(res['newick_tree_representation'].startswith("(("))

    def test_genetic_linkage(self):
        # 80 parental, 20 recombinant => r = 0.20, 20 cM
        res = GeneticLinkageMappingEngine.calculate_linkage(80, 20)
        self.assertEqual(res['standard_map_distance_cM'], "20.0 cM")
        self.assertAlmostEqual(res['recombination_fraction_r'], 0.20, places=2)

    def test_allosteric_hill_equation(self):
        # Ligand concentrations and fractional saturations mimicking positive cooperativity (nH ~ 2.8)
        concs = [0.1, 0.5, 1.0, 2.0, 5.0]
        sats = [0.005, 0.15, 0.50, 0.85, 0.98]
        res = AllostericCooperativityEngine.fit_hill_equation(concs, sats)
        self.assertTrue(res['hill_coefficient_nH'] > 1.5)
        self.assertIn("POSITIVE_COOPERATIVITY", res['cooperativity_type'])

    def test_hardy_weinberg(self):
        res = PopulationGeneticsEngine.calculate_hardy_weinberg(49, 42, 9)
        self.assertAlmostEqual(res['allele_frequency_p'], 0.7, places=2)

    def test_dna_tm(self):
        res = PureThermodynamicsEngine.calculate_melting_temp("GCGAATTCGC")
        self.assertIn('melting_temperature_Tm', res)

if __name__ == '__main__':
    unittest.main()
