import argparse
import sys
import unittest
from dredge.bio_kernel import BioChemCentumCore

def run_all():
    print("\n" + "="*65)
    print("      DREDGE v100.0.0 CENTUM BIO-CHEMICAL AUTONOMOUS CORE")
    print("                  100 SCIENTIFIC ENGINES")
    print("="*65)
    core = BioChemCentumCore()
    methods = [m for m in dir(core) if m.startswith(('bio_', 'chem_'))]
    methods.sort()
    for idx, m_name in enumerate(methods, 1):
        func = getattr(core, m_name)
        res = func()
        feat = res.pop('feature')
        params_str = ", ".join(f"{k}: {v}" for k, v in res.items())
        print(f"[{idx:03d}] {feat} -> {params_str}")
    print("="*65 + "\n")

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Centum Bio-Chemical Core (100 Features)')
    parser.add_argument('--all', action='store_true', help='Execute all 100 Biology & Chemistry engines simultaneously')
    parser.add_argument('--test', action='store_true', help='Run 100-engine unit test suite')
    parser.add_argument('--dna-thermo', nargs='?', const='GCATGCATGC', help='Bio-01: DNA Thermodynamics (Optional: SEQ)')
    parser.add_argument('--enzyme', nargs='*', type=float, help='Bio-02: Michaelis-Menten (Optional: S VMAX KM)')
    parser.add_argument('--arrhenius', nargs='*', type=float, help='Chem-51: Arrhenius Kinetics (Optional: TEMP_C EA_KJ)')
    parser.add_argument('--nernst', nargs='*', type=float, help='Chem-56: Nernst Redox (Optional: E0 N Q)')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.all:
        run_all()
        return

    if args.dna_thermo is not None:
        res = BioChemCentumCore.bio_01_dna_thermodynamics(args.dna_thermo)
        print("\n", res, "\n")
        return

    if args.enzyme is not None:
        params = args.enzyme
        if len(params) == 3: res = BioChemCentumCore.bio_02_michaelis_menten(params[0], params[1], params[2])
        else: res = BioChemCentumCore.bio_02_michaelis_menten()
        print("\n", res, "\n")
        return

    if args.arrhenius is not None:
        params = args.arrhenius
        if len(params) == 2: res = BioChemCentumCore.chem_51_arrhenius_kinetics(params[0], params[1])
        else: res = BioChemCentumCore.chem_51_arrhenius_kinetics()
        print("\n", res, "\n")
        return

    if args.nernst is not None:
        params = args.nernst
        if len(params) == 3: res = BioChemCentumCore.chem_56_nernst_redox(params[0], int(params[1]), params[2])
        else: res = BioChemCentumCore.chem_56_nernst_redox()
        print("\n", res, "\n")
        return

    run_all()

if __name__ == '__main__':
    main()
