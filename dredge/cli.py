import argparse
import sys
import unittest
from dredge.bio_kernel import (
    LatticeGaugeFieldEngine,
    RecursiveSTARKEngine,
    FractionalTurbulenceEngine,
    TensorContinuumElasticityEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Trans-Finite Mathematical Core (v70.0.0)')
    parser.add_argument('--gauge-lattice', action='store_true', help='Solve Non-Abelian SU(3) Gauge Field Wilson Loop Lattice')
    parser.add_argument('--stark-enclave', nargs='+', type=int, help='Recursive STARK AIR Constraint Proof: --stark-enclave 1 2 4 8 16 32')
    parser.add_argument('--fractal-turbulence', action='store_true', help='Simulate Fractional Navier-Stokes Turbulence Vorticity Tensor')
    parser.add_argument('--tensor-elasticity', action='store_true', help='Compute 3D Non-Linear Continuum Elasticity Stress Tensor')
    parser.add_argument('--test', action='store_true', help='Run unit tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.gauge_lattice:
        res = LatticeGaugeFieldEngine.compute_wilson_lattice(grid_size=4, beta=5.5)
        print("\n" + "="*55)
        print("  NON-ABELIAN SU(3) LATTICE GAUGE YANG-MILLS ENGINE")
        print("="*55)
        for row in res['topological_charge_tensor_ascii']:
            print("  " + row)
        print("="*55)
        print(f" • Manifold: {res['spacetime_manifold']} | Gauge: {res['gauge_group']}")
        print(f" • Mean Plaquette: {res['mean_wilson_plaquette']} | Wilson Action: {res['wilson_action_density']}\n" + "="*55 + "\n")
        return

    if args.stark_enclave:
        res = RecursiveSTARKEngine.generate_recursive_stark_proof(args.stark_enclave)
        print("\n" + "="*55)
        print("  RECURSIVE STARK ARITHMETIZATION ENCLAVE")
        print("="*55)
        print(f" • Steps: {res['computation_trace_steps']} | Reed-Solomon Domain: {res['reed_solomon_blowup_domain']}")
        print(f" • Merkle Commitment Root: {res['merkle_commitment_root']}")
        print(f" • Recursive Enclave Hash:  {res['recursive_stark_enclave_hash']}")
        print(f" • Status: {res['verification_status']} ({res['zero_knowledge_witness_leak']})\n" + "="*55 + "\n")
        return

    if args.fractal_turbulence:
        res = FractionalTurbulenceEngine.simulate_turbulence_field(grid_size=20, steps=40)
        print("\n" + "="*55)
        print("  FRACTIONAL HYDRODYNAMIC TURBULENCE VORTICITY FIELD")
        print("="*55)
        for line in res['vorticity_tensor_ascii']:
            print("  " + line)
        print("="*55)
        print(f" • Fractional Order: (-Delta)^{res['fractional_derivative_order']} | Peak Vorticity: {res['peak_vorticity']}")
        print(f" • Regime: {res['turbulence_viscosity_regime']}\n" + "="*55 + "\n")
        return

    if args.tensor_elasticity:
        grad_u = [
            [0.02, 0.01, 0.00],
            [0.01, 0.03, 0.00],
            [0.00, 0.00, 0.01]
        ]
        res = TensorContinuumElasticityEngine.compute_tensor_stress(grad_u)
        print("\n" + "="*55)
        print("  3D NON-LINEAR CONTINUUM ELASTICITY TENSOR FIELD")
        print("="*55)
        print(f" • Trace Volumetric Strain: {res['trace_volumetric_strain']}")
        print(f" • Von Mises Equivalent Stress: {res['von_mises_equivalent_stress_MPa']} MPa")
        print(f" • Status: {res['continuum_elastic_status']}")
        print(" • 2nd Piola-Kirchhoff Stress Matrix (MPa):")
        for r in res['stress_tensor_S_MPa']:
            print("   ", r)
        print("="*55 + "\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
