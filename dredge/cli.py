import argparse
import sys
import unittest
from dredge.bio_kernel import (
    DNASolitonWaveEngine,
    MultiTenantZKPedersenEngine,
    ChaosFractalDiffusionEngine,
    MacroMolecularTorsionEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Quantum-Biological Invariant Core (v68.0.0)')
    parser.add_argument('--dna-soliton', action='store_true', help='Simulate Peyrard-Bishop Non-Linear DNA Soliton Wave Dynamics')
    parser.add_argument('--zk-pedersen', nargs='+', type=int, help='Multi-Tenant Zero-Knowledge Pedersen Ledger: --zk-pedersen 500 250 1200')
    parser.add_argument('--chaos-fractal', action='store_true', help='Render Chaos-Boundary Fractal Reaction-Diffusion Lattice')
    parser.add_argument('--scaffold-strain', nargs=3, type=float, metavar=('NODES', 'TORQUE', 'AXES'), help='Compute 3D Scaffold Joint Strain')
    parser.add_argument('--test', action='store_true', help='Run unit tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.dna_soliton:
        res = DNASolitonWaveEngine.simulate_soliton_propagation(lattice_nodes=24, time_steps=60)
        print("\n" + "="*50)
        print("  DNA NON-LINEAR SOLITON WAVE MECHANICS")
        print("="*50)
        for wave in res['wave_profile_ascii']:
            print(f"  [{wave}]")
        print("="*50)
        print(f" • Peak Amplitude: {res['peak_soliton_amplitude']} Å | Speed: {res['soliton_propagation_speed']} Å/ps")
        print(f" • Verdict: {res['mechanical_stability']}\n" + "="*50 + "\n")
        return

    if args.zk_pedersen:
        res = MultiTenantZKPedersenEngine.verify_multi_tenant_state(args.zk_pedersen)
        print("\n" + "="*50)
        print("  MULTI-TENANT ZK-PEDERSEN STATE MATRIX")
        print("="*50)
        for t in res['tenant_commitments']:
            print(f" • {t['tenant_id']}: Commitment = {t['commitment']}")
        print(f" • Aggregated Commitment: {res['aggregated_homomorphic_commitment']}")
        print(f" • Proof Status: {res['zk_proof_status']} ({res['privacy_metric']})\n" + "="*50 + "\n")
        return

    if args.chaos_fractal:
        res = ChaosFractalDiffusionEngine.simulate_chaos_fractal(grid_size=24, steps=70)
        print("\n" + "="*50)
        print("  CHAOS-BOUNDARY FRACTAL REACTION-DIFFUSION")
        print("="*50)
        for line in res['fractal_ascii_tissue']:
            print("  " + line)
        print("="*50)
        print(f" • Attractor State: {res['chaos_attractor_state']} | Fractal Area: {res['fractal_occupancy_pct']}\n")
        return

    if args.scaffold_strain:
        res = MacroMolecularTorsionEngine.calculate_scaffold_strain(int(args.scaffold_strain[0]), args.scaffold_strain[1], int(args.scaffold_strain[2]))
        print(f"\n • Scaffold: {res['topological_scaffold_nodes']} Nodes ({res['spatial_coordination_axes']} Axes, {res['intersecting_joints']} Joints)\n • Von Mises Stress: {res['von_mises_stress_MPa']} MPa | Strain Energy: {res['joint_strain_energy_J']} J ({res['structural_verdict']})\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
