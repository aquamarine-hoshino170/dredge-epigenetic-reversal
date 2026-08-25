import argparse
import sys
import unittest
from dredge.bio_kernel import (
    NLSESolitonSolverEngine,
    HomomorphicMatrixLedgerEngine,
    MacroMolecularMeshTorsionEngine,
    FractionalDiffusionFractalEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Universal Singularity Multi-Domain Core (v69.0.0)')
    parser.add_argument('--schrodinger-soliton', action='store_true', help='Solve Non-Linear Schrodinger Equation (NLSE) Soliton Grid')
    parser.add_argument('--homomorphic-ledger', nargs='+', type=int, help='Multi-Tenant Homomorphic Private Matrix Ledger: --homomorphic-ledger 600 300 1500')
    parser.add_argument('--mesh-torsion', nargs=3, type=float, metavar=('NODES', 'TORQUE', 'AXES'), help='3D Macro-Molecular Joint Mesh Optimization')
    parser.add_argument('--fractal-diffusion', action='store_true', help='Render Dynamic Fractional-Diffusion Spatial Lattice')
    parser.add_argument('--test', action='store_true', help='Run unit tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.schrodinger_soliton:
        res = NLSESolitonSolverEngine.solve_soliton_grid(nodes=32, time_steps=50)
        print("\n" + "="*55)
        print("  NON-LINEAR SCHRODINGER EQUATION (NLSE) SOLITON SOLVER")
        print("="*55)
        for p in res['density_ascii_plots']:
            print(f"  [{p}]")
        print("="*55)
        print(f" • Grid Nodes: {res['spatial_grid_nodes']} | Peak Density: {res['peak_soliton_density']}")
        print(f" • Stability: {res['phase_envelope_stability']}\n" + "="*55 + "\n")
        return

    if args.homomorphic_ledger:
        res = HomomorphicMatrixLedgerEngine.verify_ledger(args.homomorphic_ledger)
        print("\n" + "="*55)
        print("  DECENTRALIZED HOMOMORPHIC PRIVATE MATRIX LEDGER")
        print("="*55)
        for c in res['node_commitments']:
            print(f" • {c['client_node']}: Vector Commitment = {c['vector_commitment']}")
        print(f" • Aggregated Proof: {res['aggregated_homomorphic_proof']}")
        print(f" • Status: {res['proof_validation_status']} ({res['cryptographic_integrity']})\n" + "="*55 + "\n")
        return

    if args.mesh_torsion:
        res = MacroMolecularMeshTorsionEngine.calculate_mesh_torsion(int(args.mesh_torsion[0]), args.mesh_torsion[1], int(args.mesh_torsion[2]))
        print(f"\n • Joint Mesh: {res['topological_nodes']} Nodes ({res['spatial_axes']} Axes, {res['joint_intersections']} Intersections)\n • Von Mises Stress: {res['von_mises_stress_MPa']} MPa (Normal: {res['normal_stress_MPa']}, Shear: {res['shear_stress_MPa']})\n • Strain Energy: {res['joint_strain_energy_J']} J ({res['structural_verdict']})\n")
        return

    if args.fractal_diffusion:
        res = FractionalDiffusionFractalEngine.simulate_fractal_lattice(grid_size=24, steps=70)
        print("\n" + "="*55)
        print("  DYNAMIC FRACTIONAL-DIFFUSION FRACTAL LATTICE")
        print("="*55)
        for line in res['fractal_ascii_tissue']:
            print("  " + line)
        print("="*55)
        print(f" • Attractor State: {res['chaos_attractor_state']} | Fractal Area: {res['fractal_occupancy_pct']}\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
