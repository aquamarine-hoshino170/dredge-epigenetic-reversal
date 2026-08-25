import argparse
import sys
import unittest
from dredge.bio_kernel import (
    HeterogeneousPolyglotQuineEngine,
    MultiTenantZKPedersenEngine,
    ChaosFractalDiffusionEngine,
    MultiAxisLatticeOptimizationEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Logic Singularity Suite (v67.0.0)')
    parser.add_argument('--polyglot-quine', nargs='?', const='c', default=None, help='Synthesize Polyglot Quine Module (c/js)')
    parser.add_argument('--zk-pedersen', nargs='+', type=int, help='Multi-Tenant Zero-Knowledge Pedersen Ledger: --zk-pedersen 500 250 1200')
    parser.add_argument('--chaos-fractal', action='store_true', help='Render Chaos-Boundary Fractal Reaction-Diffusion Lattice')
    parser.add_argument('--mesh-top', nargs=3, type=float, metavar=('NODES', 'TORQUE', 'AXES'), help='Multi-Axis Lattice Topological Optimization')
    parser.add_argument('--test', action='store_true', help='Run unit tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.polyglot_quine:
        res = HeterogeneousPolyglotQuineEngine.synthesize_polyglot(args.polyglot_quine)
        print("\n" + "="*50)
        print(f"  HETEROGENEOUS POLYGLOT QUINE ({res['target_paradigm']})")
        print("="*50)
        print(f" • Signature: {res['payload_signature']} | SHA-256: {res['root_sha256_verification'][:16]}...")
        print(" • Synthesized Source Output:\n")
        print(res['generated_polyglot_source'])
        print("\n" + "="*50 + "\n")
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

    if args.mesh_top:
        res = MultiAxisLatticeOptimizationEngine.optimize_structural_lattice(int(args.mesh_top[0]), args.mesh_top[1], int(args.mesh_top[2]))
        print(f"\n • Lattice Mesh: {res['topological_nodes']} Nodes ({res['spatial_coordination_axes']} Axes, {res['mesh_intersections']} Intersections)\n • Von Mises Stress: {res['von_mises_equivalent_stress_MPa']} MPa (Normal: {res['normal_stress_MPa']}, Shear: {res['shear_stress_MPa']})\n • Strain Energy: {res['strain_energy_J']} J ({res['structural_evaluation']})\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
