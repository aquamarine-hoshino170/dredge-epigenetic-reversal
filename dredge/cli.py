import argparse
import sys
import unittest
from dredge.bio_kernel import (
    QuantumComputingCore,
    CellularMorphogenesisCore,
    InformationSignalPhysicsCore,
    OrbitalAstrophysicsCore
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Omniscience Singularity Suite (v85.0.0)')
    parser.add_argument('--quantum-circuit', action='store_true', help='Simulate 2-Qubit Bell State Entanglement & Gate Matrix')
    parser.add_argument('--cellular-life', action='store_true', help='Execute Morphogenesis Automata & Shannon Entropy Evolution')
    parser.add_argument('--signal-fft', action='store_true', help='Compute Cooley-Tukey FFT Power Spectral Density (PSD)')
    parser.add_argument('--orbital-nbody', action='store_true', help='Simulate Symplectic Velocity-Verlet Orbit & Lagrange Points')
    parser.add_argument('--test', action='store_true', help='Run unit tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.quantum_circuit:
        res = QuantumComputingCore.simulate_bell_state()
        print("\n" + "="*55)
        print("  QUANTUM COMPUTING: 2-QUBIT BELL ENTANGLEMENT")
        print("="*55)
        print(f" • System: {res['qubit_system']}")
        print(f" • State Amplitudes: {res['state_vector_amplitudes']}")
        print(" • Basis Probabilities:")
        for k, v in res['basis_probabilities'].items():
            print(f"   {k}: {v * 100:.1f}%")
        print(f" • Verdict: {res['entanglement_verdict']}\n" + "="*55 + "\n")
        return

    if args.cellular_life:
        res = CellularMorphogenesisCore.simulate_automata(grid_size=16, steps=15)
        print("\n" + "="*55)
        print("  COMPLEX SYSTEMS: CELLULAR MORPHOGENESIS")
        print("="*55)
        for row in res['terminal_morphology_ascii']:
            print("  [" + row + "]")
        print("="*55)
        print(f" • Final Shannon Entropy: {res['final_shannon_entropy']} bits")
        print(f" • Entropy Gradient: {res['entropy_gradient']}")
        print(f" • Dynamics: {res['morphogenesis_verdict']}\n" + "="*55 + "\n")
        return

    if args.signal_fft:
        res = InformationSignalPhysicsCore.analyze_signal(num_samples=64, f1=6.0, f2=14.0)
        print("\n" + "="*55)
        print("  INFORMATION PHYSICS: COOLEY-TUKEY FFT PSD PLOT")
        print("="*55)
        print(f"  [{res['spectral_density_ascii']}]")
        print("="*55)
        print(f" • Samples: {res['total_samples']} | Nyquist: {res['nyquist_frequency_hz']} Hz")
        print(f" • Peak Power Spectral Density: {res['dominant_peak_psd']}\n" + "="*55 + "\n")
        return

    if args.orbital_nbody:
        res = OrbitalAstrophysicsCore.simulate_two_body_orbit(time_steps=50)
        print("\n" + "="*55)
        print("  ASTROPHYSICS: SYMPLECTIC ORBITAL MECHANICS")
        print("="*55)
        print(f" • Semi-Major Axis Radius: {res['semi_major_axis']} AU")
        print(f" • Orbital Energy: {res['orbital_energy_conservation']}")
        print(f" • Lagrange L1 Radius: {res['lagrange_point_L1_radius']} AU")
        print(f" • Verdict: {res['symplectic_stability']}\n" + "="*55 + "\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
