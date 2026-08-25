import argparse
import sys
import unittest
from dredge.bio_kernel import (
    AsyncP2PBioLedgerEngine,
    QuantumLindbladDensityVisualizerEngine,
    TuringMorphogenesisDynamicGridEngine,
    DNAOrigamiTorsionRouterEngine,
    ChronomorphicShannonManifoldEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Hyper-Dimensional Quantum Automata Suite (v60.0.0)')
    parser.add_argument('--async-ledger', nargs='+', help='Run Asynchronous P2P Bio-Consensus: --async-ledger MUT_A12T MUT_G88C')
    parser.add_argument('--lindblad-vis', action='store_true', help='Visualize Quantum Lindblad Density Matrix & Coherence')
    parser.add_argument('--turing-mask', action='store_true', help='Render 2D Turing Morphogenesis with Boundary Mask')
    parser.add_argument('--origami-3d', nargs=3, type=int, metavar=('SCAFFOLD', 'STAPLES', 'PLANES'), help='3D DNA Origami Torsion Router')
    parser.add_argument('--chrono-shannon', nargs=1, type=int, metavar=('GENERATIONS',), help='Chronomorphic Shannon Manifold Decay')
    parser.add_argument('--test', action='store_true', help='Run unit tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.async_ledger:
        res = AsyncP2PBioLedgerEngine.run_consensus_mesh(args.async_ledger, num_nodes=3)
        print("\n" + "="*55)
        print("  ASYNCHRONOUS P2P PROOF-OF-SEQUENCE CONSENSUS LEDGER")
        print("="*55)
        for b in res['chain_ledger']:
            print(f" Block #{b['block_index']} | Node: {b['mined_by_node']} | Data: {b['mutation_payload']} | Hash: {b['block_hash'][:14]}... | Nonce: {b['nonce']}")
        print("="*55 + "\n")
        return

    if args.lindblad_vis:
        res = QuantumLindbladDensityVisualizerEngine.simulate_and_visualize(sites=4, total_time_fs=40.0)
        print("\n" + "="*45)
        print("  QUANTUM LINDBLAD DENSITY MATRIX MAGNITUDE")
        print("="*45)
        for row in res['density_matrix_ascii']:
            print("   " + row)
        print("="*45)
        print(f" • Site Exciton Populations: {res['site_populations']}\n • Max Cross-Coherence |rho_ij|: {res['max_cross_coherence']}\n")
        return

    if args.turing_mask:
        res = TuringMorphogenesisDynamicGridEngine.render_morphogenesis(grid_size=20, iterations=80)
        print("\n" + "="*45)
        print("  2D TURING MORPHOGENESIS BOUNDARY LATTICE")
        print("="*45)
        for r in res['ascii_tissue_render']:
            print("  " + r)
        print("="*45)
        print(f" • Active Tissue Area: {res['active_tissue_area_pct']} | Mean Activator: {res['mean_activator_density']}\n")
        return

    if args.origami_3d:
        res = DNAOrigamiTorsionRouterEngine.calculate_routing_strain(args.origami_3d[0], args.origami_3d[1], args.origami_3d[2])
        print(f"\n • 3D DNA Origami: {res['scaffold_length_bp']} bp ({res['spatial_target_planes']} Planes) | Crossovers: {res['optimal_crossovers']}\n • Torsion Strain Energy: {res['torsion_strain_energy_pN_nm']} pN·nm ({res['stability_status']})\n")
        return

    if args.chrono_shannon:
        res = ChronomorphicShannonManifoldEngine.simulate_entropy_manifold(generations=args.chrono_shannon[0])
        print(f"\n • Chronomorphic Epigenetic Shannon: Retained = {res['final_retained_entropy']} bits (Loss: {res['entropy_loss_pct']})\n • Trajectory: {res['decay_trajectory']}\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
