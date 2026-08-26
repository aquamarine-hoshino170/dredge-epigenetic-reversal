import argparse
import sys
import unittest
from dredge.bio_kernel import (
    PureMathCore,
    PureBiologyCore,
    PurePhysicsCore,
    PureChemistryCore
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Pure Science & Mathematical Core (v80.0.0)')
    parser.add_argument('--math-curvature', action='store_true', help='Compute 2D Manifold Riemann Ricci Scalar Curvature')
    parser.add_argument('--bio-thermo', nargs=1, type=str, metavar=('DNA_SEQ',), help='DNA Melting Temp & Nearest-Neighbor Free Energy')
    parser.add_argument('--physics-wave', action='store_true', help='Simulate Quantum Wave Packet Dispersive Expansion')
    parser.add_argument('--chem-kinetics', nargs=2, type=float, metavar=('TEMP_C', 'EA_KJ'), help='Compute Arrhenius Kinetics & Rate Constant')
    parser.add_argument('--test', action='store_true', help='Run unit tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.math_curvature:
        metric = [[2.0, 0.5], [0.5, 3.0]]
        res = PureMathCore.calculate_curvature(metric)
        print("\n" + "="*55)
        print("  PURE MATHEMATICS: RIEMANNIAN RICCI CURVATURE")
        print("="*55)
        print(f" • Determinant: {res['metric_determinant']} | Ricci Scalar: {res['ricci_scalar_curvature']}")
        print(f" • Manifold Status: {res['manifold_status']}\n" + "="*55 + "\n")
        return

    if args.bio_thermo:
        res = PureBiologyCore.calculate_dna_thermodynamics(args.bio_thermo[0])
        print("\n" + "="*55)
        print("  PURE BIOLOGY: DNA THERMODYNAMICS & MELTING CORE")
        print("="*55)
        print(f" • Sequence Length: {res['sequence_length']}")
        print(f" • Enthalpy (ΔH): {res['enthalpy_delta_H_kcal_mol']} kcal/mol | Entropy (ΔS): {res['entropy_delta_S_cal_k_mol']} cal/K·mol")
        print(f" • Free Energy (ΔG 37°C): {res['free_energy_delta_G_37C']} kcal/mol")
        print(f" • Melting Temp (Tm): {res['melting_temperature_Tm_C']} °C ({res['thermodynamic_stability']})\n" + "="*55 + "\n")
        return

    if args.physics_wave:
        res = PurePhysicsCore.simulate_quantum_dispersion(nodes=24, time_fs=20.0)
        print("\n" + "="*55)
        print("  PURE PHYSICS: QUANTUM DISPERSION WAVE PACKET")
        print("="*55)
        print(f"  [{res['quantum_wave_profile']}]")
        print("="*55)
        print(f" • Evolution Time: {res['evolution_time_fs']} fs | Wave Width (σ): {res['dispersed_width_sigma_t']}")
        print(f" • Peak Density: {res['peak_probability_density']}\n" + "="*55 + "\n")
        return

    if args.chem_kinetics:
        res = PureChemistryCore.compute_reaction_rate(args.chem_kinetics[0], args.chem_kinetics[1])
        print("\n" + "="*55)
        print("  PURE CHEMISTRY: ARRHENIUS REACTION KINETICS")
        print("="*55)
        print(f" • Temperature: {res['temperature_kelvin']} K | Activation Energy: {res['activation_energy_Ea']}")
        print(f" • Rate Constant (k): {res['rate_constant_k']}")
        print(f" • Regime: {res['kinetic_regime']}\n" + "="*55 + "\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
