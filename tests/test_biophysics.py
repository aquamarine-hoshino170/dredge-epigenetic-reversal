import unittest
import numpy as np
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
        # SantaLucia Reference Test
        res = PureThermodynamicsEngine.calculate_melting_temp("GCGAATTCGC")
        self.assertIn("melting_temperature_Tm", res)
        self.assertTrue(res["enthalpy_dH_kcal_mol"] < 0)

    def test_protein_isoelectric_point(self):
        # Aspartate rich peptide should have an acidic pI (< 5.0)
        res = PureBiochemistryProteinEngine.calculate_isoelectric_point("DDDDDD")
        self.assertTrue(res["isoelectric_point_pI"] < 4.0)

    def test_ribosomal_translation(self):
        # Start codon + Alanine + Stop codon
        peptide = PureMolecularGenomicsEngine.translate("ATGGCTTAA")
        self.assertEqual(peptide, "MA*")

    def test_enzyme_kinetics_lineweaver(self):
        # Theoretical values: Vmax = 100, Km = 10
        substrates = [5.0, 10.0, 20.0, 40.0]
        velocities = [(100.0 * s) / (10.0 + s) for s in substrates]
        res = PureEnzymeKineticsEngine.fit_lineweaver_burk(substrates, velocities)
        self.assertAlmostEqual(res["v_max"], 100.0, places=2)
        self.assertAlmostEqual(res["k_m"], 10.0, places=2)
        self.assertAlmostEqual(res["r_squared"], 1.0, places=2)

    def test_buffer_ph(self):
        # Equimolar weak acid and conjugate base => pH == pKa
        res = PureBufferEquilibriumEngine.calculate_buffer_ph(pka=4.76, conjugate_base_conc=0.1, weak_acid_conc=0.1)
        self.assertAlmostEqual(res["equilibrium_ph"], 4.76, places=2)

    def test_spectrophotometry(self):
        # Pure dsDNA standard
        res = PureSpectrophotometryEngine.quantify_nucleic_acid(a260=1.0, a280=0.53, sample_type="dsdna")
        self.assertEqual(res["concentration_ng_ul"], 50.0)
        self.assertIn("HIGH_PURITY", res["purity_assessment"])

if __name__ == "__main__":
    unittest.main()
