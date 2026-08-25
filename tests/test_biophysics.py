import unittest
from dredge.bio_kernel import (
    PureThermodynamicsEngine, PureBiochemistryProteinEngine, BigDataGenomicsEngine, FastqQualityFilterEngine
)

class TestBigDataBiophysics(unittest.TestCase):
    def test_bwt(self):
        res = BigDataGenomicsEngine.burrows_wheeler_transform("BANANA")
        self.assertEqual(res['bwt_transformed'], "ANNB$AA")

    def test_global_align(self):
        res = BigDataGenomicsEngine.needleman_wunsch_global_align("GATTACA", "GCATGCU")
        self.assertIn('global_alignment_score', res)

    def test_tm(self):
        res = PureThermodynamicsEngine.calculate_melting_temp("GCGAATTCGC")
        self.assertIn('melting_temperature_Tm', res)

    def test_fastq_qc(self):
        # 'I' in Phred+33 is Q40 (high quality)
        res = FastqQualityFilterEngine.filter_read("ATGC", "IIII")
        self.assertEqual(res['quality_filter_status'], "PASS")
        self.assertEqual(res['mean_phred_score'], 40.0)

if __name__ == '__main__':
    unittest.main()
