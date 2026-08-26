import argparse
import sys
import unittest
from dredge.bio_kernel import (
    NLSESolitonSolverEngine,
    LatticeGaugeFieldEngine,
    RecursiveSTARKEngine,
    TensorContinuumElasticityEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Pure Autonomous Core (v75.0.0)')
    parser.add_argument('--schrodinger-soliton', action='store_true', help='Solve Non-Linear Schrodinger Equation (NLSE) Soliton Grid')
    parser.add_argument('--gauge-lattice', action='store_true', help='Solve Non-Abelian SU(3) Gauge Field Wilson Plaquette Lattice')
    parser.add_argument('--stark-enclave', nargs='+', type=int, help='Recursive STARK Proof: --stark-enclave 1 2 4 8 16 32')
    parser.add_argument('--tensor-elasticity', action='store_true', help='Compute 3D Non-Linear Continuum Elasticity Stress Tensor')
    parser.add_argument('--test', action='store_true', help='Run unit tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.schrodinger_soliton:
        res = NLSESolitonSolverEngine.solve_soliton_grid(nodes=32, time_steps=40)
        print("\n" + "="*55)
        print("  NLSE SOLITON GRID SOLVER (ZERO DEPENDENCY)")
        print("="*55)
        for p in res['density_ascii_plots']:
            print(f"  [{p}]")
        print("="*55)
        print(f" • Grid Nodes: {res['spatial_grid_nodes']} | Peak Density: {res['peak_soliton_density']}\n • Stability: {res['phase_envelope_stability']}\n" + "="*55 + "\n")
        return

    if args.gauge_lattice:
        res = LatticeGaugeFieldEngine.compute_wilson_lattice(grid_size=4, beta=5.5)
        print("\n" + "="*55)
        print("  NON-ABELIAN SU(3) LATTICE GAUGE YANG-MILLS")
        print("="*55)
        for row in res['topological_charge_tensor_ascii']:
            print("  " + row)
        print("="*55)
        print(f" • Manifold: {res['spacetime_manifold']}\n • Mean Plaquette: {res['mean_wilson_plaquette']} | Action: {res['wilson_action_density']}\n" + "="*55 + "\n")
        return

    if args.stark_enclave:
        res = RecursiveSTARKEngine.generate_recursive_stark_proof(args.stark_enclave)
        print("\n" + "="*55)
        print("  RECURSIVE STARK ARITHMETIZATION ENCLAVE")
        print("="*55)
        print(f" • Steps: {res['computation_trace_steps']}")
        print(f" • Merkle Root: {res['merkle_commitment_root']}")
        print(f" • Recursive Hash: {res['recursive_stark_enclave_hash']}")
        print(f" • Status: {res['verification_status']} ({res['zero_knowledge_witness_leak']})\n" + "="*55 + "\n")
        return

    if args.tensor_elasticity:
        grad_u = [
            [0.02, 0.01, 0.00],
            [0.01, 0.03, 0.00],
            [0.00, 0.00, 0.01]
        ]
        res = TensorContinuumElasticityEngine.compute_tensor_stress(grad_u)
        print("\n" + "="*55)
        print("  3D CONTINUUM ELASTICITY TENSOR FIELD")
        print("="*55)
        print(f" • Volumetric Strain: {res['trace_volumetric_strain']}")
        print(f" • Von Mises Stress: {res['von_mises_equivalent_stress_MPa']} MPa")
        print(" • Stress Matrix S (MPa):")
        for r in res['stress_tensor_S_MPa']:
            print("   ", r)
        print("="*55 + "\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
