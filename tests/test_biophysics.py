import unittest
from dredge.bio_kernel import BioChemCentumCore

class TestCentumBioChemCore(unittest.TestCase):
    def test_all_100_engines(self):
        core = BioChemCentumCore()
        methods = [m for m in dir(core) if m.startswith(('bio_', 'chem_'))]
        self.assertEqual(len(methods), 100, "Must have exactly 100 biology and chemistry features")
        for m_name in methods:
            func = getattr(core, m_name)
            res = func()
            self.assertIsInstance(res, dict)
            self.assertIn('feature', res)

if __name__ == '__main__':
    unittest.main()
