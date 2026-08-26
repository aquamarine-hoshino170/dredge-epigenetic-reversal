import argparse
import unittest
from dredge.physics import QuantumCore, SignalCore, OrbitalCore
from dredge.biology import BiologyCore
from dredge.chemistry import ChemistryCore
from dredge.math_crypto import MathCore, CryptoCore

def run_all():
    print("\n" + "="*60)
    print("       DREDGE v115.0.0 REAL SCIENTIFIC MODULAR CORE")
    print("="*60)
    print(" • [Physics/Quantum Bell]:", QuantumCore.simulate_bell_pair())
    print(" • [Physics/Orbital]:", OrbitalCore.step_orbit())
    print(" • [Biology/DNA Thermo]:", BiologyCore.dna_thermodynamics())
    print(" • [Biology/Enzyme]:", BiologyCore.michaelis_menten())
    print(" • [Chemistry/Arrhenius]:", ChemistryCore.arrhenius_rate())
    print(" • [Chemistry/Nernst]:", ChemistryCore.nernst_redox())
    print(" • [Math/Ricci Curvature]:", MathCore.riemann_ricci_curvature())
    print(" • [Crypto/Pedersen Ledger]:", CryptoCore.verify_ledger())
    print("="*60 + "\n")

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='Real Scientific & Mathematical Core')
    parser.add_argument('--all', action='store_true', help='Run all real scientific engines')
    parser.add_argument('--quantum', action='store_true', help='Simulate Quantum Bell State')
    parser.add_argument('--orbit', action='store_true', help='Run Symplectic Orbital Step')
    parser.add_argument('--dna', nargs='?', const='GCATGCATGC', help='DNA Nearest-Neighbor Thermodynamics (Optional: SEQ)')
    parser.add_argument('--enzyme', nargs='*', type=float, help='Enzyme Kinetics (Optional: S VMAX KM)')
    parser.add_argument('--arrhenius', nargs='*', type=float, help='Arrhenius Rate (Optional: TEMP_C EA_KJ)')
    parser.add_argument('--nernst', nargs='*', type=float, help='Nernst Redox Potential (Optional: E0 N Q)')
    parser.add_argument('--curvature', action='store_true', help='Riemann Ricci Curvature')
    parser.add_argument('--ledger', nargs='+', type=int, help='Pedersen Homomorphic Ledger')
    parser.add_argument('--test', action='store_true', help='Run Regression Unit Tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.all: run_all(); return
    if args.quantum: print("\n", QuantumCore.simulate_bell_pair(), "\n"); return
    if args.orbit: print("\n", OrbitalCore.step_orbit(), "\n"); return
    if args.dna is not None: print("\n", BiologyCore.dna_thermodynamics(args.dna), "\n"); return
    if args.enzyme is not None:
        p = args.enzyme
        res = BiologyCore.michaelis_menten(p[0], p[1], p[2]) if len(p) == 3 else BiologyCore.michaelis_menten()
        print("\n", res, "\n"); return
    if args.arrhenius is not None:
        p = args.arrhenius
        res = ChemistryCore.arrhenius_rate(p[0], p[1]) if len(p) == 2 else ChemistryCore.arrhenius_rate()
        print("\n", res, "\n"); return
    if args.nernst is not None:
        p = args.nernst
        res = ChemistryCore.nernst_redox(p[0], int(p[1]), p[2]) if len(p) == 3 else ChemistryCore.nernst_redox()
        print("\n", res, "\n"); return
    if args.curvature: print("\n", MathCore.riemann_ricci_curvature(), "\n"); return
    if args.ledger: print("\n", CryptoCore.verify_ledger(args.ledger), "\n"); return

    run_all()

if __name__ == '__main__':
    main()
