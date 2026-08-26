import argparse
import sys
import unittest
from dredge.bio_kernel import (
    QuantumComputingCore,
    CellularMorphogenesisCore,
    InformationSignalPhysicsCore,
    OrbitalAstrophysicsCore,
    PureMathCore,
    PureBiologyCore,
    PurePhysicsCore,
    PureChemistryCore,
    ZeroKnowledgePedersenEngine,
    TensorContinuumElasticityEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Deca-Domain Omniscience Core (v90.0.0)')
    parser.add_argument('--quantum-circuit', action='store_true', help='1. Quantum Bell State Entanglement')
    parser.add_argument('--cellular-life', action='store_true', help='2. Cellular Morphogenesis & Shannon Entropy')
    parser.add_argument('--signal-fft', action='store_true', help='3. Cooley-Tukey FFT PSD Plot')
    parser.add_argument('--orbital-nbody', action='store_true', help='4. Symplectic Verlet Orbital Mechanics')
    parser.add_argument('--math-curvature', action='store_true', help='5. Riemannian Ricci Scalar Curvature')
    parser.add_argument('--bio-thermo', nargs=1, type=str, metavar=('DNA_SEQ',), help='6. DNA Melting Temp & Free Energy')
    parser.add_argument('--physics-wave', action='store_true', help='7. Quantum Wave Packet Dispersion')
    parser.add_argument('--chem-kinetics', nargs=2, type=float, metavar=('TEMP_C', 'EA_KJ'), help='8. Arrhenius Reaction Kinetics')
    parser.add_argument('--zk-pedersen', nargs='+', type=int, help='9. ZK-Pedersen Ledger Homomorphic Proof')
    parser.add_argument('--tensor-elasticity', action='store_true', help='10. 3D Non-Linear Continuum Elasticity')
    parser.add_argument('--test', action='store_true', help='Run 10-Domain Unit Tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.quantum_circuit:
        res = QuantumComputingCore.simulate_bell_state()
        print(f"\n[1. Quantum Core] System: {res['qubit_system']} | Probabilities: {res['basis_probabilities']}\n")
        return

    if args.cellular_life:
        res = CellularMorphogenesisCore.simulate_automata(grid_size=16, steps=15)
        print(f"\n[2. Cellular Core] Shannon Entropy: {res['final_shannon_entropy']} bits ({res['morphogenesis_verdict']})\n")
        return

    if args.signal_fft:
        res = InformationSignalPhysicsCore.analyze_signal(num_samples=64)
        print(f"\n[3. Signal FFT] PSD Spectrum: [{res['spectral_density_ascii']}] | Peak: {res['dominant_peak_psd']}\n")
        return

    if args.orbital_nbody:
        res = OrbitalAstrophysicsCore.simulate_two_body_orbit(time_steps=40)
        print(f"\n[4. Orbital Core] Radius: {res['semi_major_axis']} AU | L1 Radius: {res['lagrange_point_L1_radius']} AU\n")
        return

    if args.math_curvature:
        res = PureMathCore.calculate_curvature([[2.0, 0.5], [0.5, 3.0]])
        print(f"\n[5. Pure Math] Determinant: {res['metric_determinant']} | Ricci Curvature: {res['ricci_scalar_curvature']}\n")
        return

    if args.bio_thermo:
        res = PureBiologyCore.calculate_dna_thermodynamics(args.bio_thermo[0])
        print(f"\n[6. Pure Bio] Sequence: {res['sequence_length']} | Tm: {res['melting_temperature_Tm_C']} °C | ΔG: {res['free_energy_delta_G_37C']} kcal/mol\n")
        return

    if args.physics_wave:
        res = PurePhysicsCore.simulate_quantum_dispersion(nodes=24, time_fs=20.0)
        print(f"\n[7. Pure Physics] Wave: [{res['quantum_wave_profile']}] | Width (σ): {res['dispersed_width_sigma_t']}\n")
        return

    if args.chem_kinetics:
        res = PureChemistryCore.compute_reaction_rate(args.chem_kinetics[0], args.chem_kinetics[1])
        print(f"\n[8. Pure Chem] Rate Constant (k): {res['rate_constant_k']} ({res['kinetic_regime']})\n")
        return

    if args.zk_pedersen:
        res = ZeroKnowledgePedersenEngine.verify_ledger(args.zk_pedersen)
        print(f"\n[9. ZK Ledger] Proof: {res['aggregated_homomorphic_proof']} | Status: {res['proof_validation_status']}\n")
        return

    if args.tensor_elasticity:
        grad_u = [[0.02, 0.01, 0.00], [0.01, 0.03, 0.00], [0.00, 0.00, 0.01]]
        res = TensorContinuumElasticityEngine.compute_tensor_stress(grad_u)
        print(f"\n[10. Tensor Elasticity] Von Mises Stress: {res['von_mises_equivalent_stress_MPa']} MPa ({res['continuum_elastic_status']})\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
