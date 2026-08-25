import argparse
import sys
import unittest
from dredge.bio_kernel import (
    PolymorphicQuineEngine,
    ZeroKnowledgeLedgerEngine,
    ChaosReactionDiffusionEngine,
    MolecularMeshStrainEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Polymorphic & Zero-Knowledge Core (v66.0.0)')
    parser.add_argument('--poly-quine', action='store_true', help='Generate Polymorphic Self-Replicating Code Replica')
    parser.add_argument('--zk-ledger', nargs=2, type=int, metavar=('BALANCE', 'TRANSFER'), help='Simulate Zero-Knowledge Pedersen Commitment Transition')
    parser.add_argument('--chaos-rd', action='store_true', help='Render Chaos-Boundary Reaction-Diffusion Lattice')
    parser.add_argument('--mesh-strain', nargs=3, type=float, metavar=('NODES', 'DENSITY', 'TORQUE'), help='Compute Molecular Mesh Topological Strain')
    parser.add_argument('--test', action='store_true', help='Run unit tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.poly_quine:
        res = PolymorphicQuineEngine.generate_polymorphic_replica()
        print("\n" + "="*50)
        print("  POLYMORPHIC QUINE REPLICA GENERATOR")
        print("="*50)
        print(f" • Signature: {res['polymorphic_signature']} | Bytes: {res['generated_code_bytes']}")
        print(" • Code Output:\n")
        print(res['source_code_replica'])
        print("\n" + "="*50 + "\n")
        return

    if args.zk_ledger:
        res = ZeroKnowledgeLedgerEngine.simulate_zk_transition(args.zk_ledger[0], args.zk_ledger[1])
        print("\n" + "="*50)
        print("  ZERO-KNOWLEDGE PEDERSEN COMMITMENT LEDGER")
        print("="*50)
        print(f" • Initial Commitment:   {res['commitment_initial']}")
        print(f" • Transfer Commitment:  {res['commitment_transfer']}")
        print(f" • Remainder Commitment: {res['commitment_remainder']}")
        print(f" • Cryptographic Proof:  {res['zk_proof_verified']} ({res['privacy_status']})\n" + "="*50 + "\n")
        return

    if args.chaos_rd:
        res = ChaosReactionDiffusionEngine.simulate_chaos_lattice(grid_size=20, steps=60)
        print("\n" + "="*45)
        print("  CHAOS-BOUNDARY REACTION-DIFFUSION LATTICE")
        print("="*45)
        for row in res['ascii_visual']:
            print("  " + row)
        print("="*45)
        print(f" • Attractor State: {res['chaos_attractor_state']} | Mean Field: {res['mean_field_density']}\n")
        return

    if args.mesh_strain:
        res = MolecularMeshStrainEngine.calculate_mesh_strain(int(args.mesh_strain[0]), args.mesh_strain[1], args.mesh_strain[2])
        print(f"\n • Molecular Mesh: {res['scaffold_topological_nodes']} Nodes, {res['interconnecting_mesh_edges']} Edges\n • Shear Strain: {res['shear_strain_magnitude']} | Energy: {res['total_strain_energy_J']} J ({res['topological_stability']})\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
