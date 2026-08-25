import argparse
import sys
import unittest
from dredge.bio_kernel import (
    DynamicTopologyP2PLedgerEngine,
    OpenQuantumLindbladVisualizerEngine,
    FractalTuringMorphogenesisEngine,
    MultiAxisOrigamiTorsionEngine,
    DeepChronomorphicShannonEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Trans-Computational Quantum Bio-OS Core (v61.0.0)')
    parser.add_argument('--mesh-ledger', nargs='+', help='Dynamic P2P Bio-Consensus Mesh: --mesh-ledger MUT_1 MUT_2')
    parser.add_argument('--lindblad-env', action='store_true', help='Open Quantum Lindblad Visualizer with Environmental Noise')
    parser.add_argument('--fractal-turing', action='store_true', help='Render 2D Fractal-Boundary Turing Morphogenesis')
    parser.add_argument('--origami-axes', nargs=4, type=int, metavar=('BP', 'STAPLES', 'AXES', 'HINGES'), help='Multi-Axis DNA Origami Torsion Router')
    parser.add_argument('--deep-chrono', nargs=1, type=int, metavar=('GENS',), help='Deep Temporal Chronomorphic Shannon Decay')
    parser.add_argument('--test', action='store_true', help='Run unit tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.mesh_ledger:
        res = DynamicTopologyP2PLedgerEngine.run_dynamic_mesh(args.mesh_ledger, total_nodes=6, clusters=2)
        print("\n" + "="*60)
        print("  DYNAMIC TOPOLOGY P2P PROOF-OF-SEQUENCE CONSENSUS MESH")
        print("="*60)
        for b in res['consensus_ledger']:
            print(f" Block #{b['block_index']} | Cluster: {b['cluster_id']} | Node: {b['mined_by_node']} | Data: {b['mutation']} | Hash: {b['block_hash'][:14]}...")
        print("="*60 + "\n")
        return

    if args.lindblad_env:
        res = OpenQuantumLindbladVisualizerEngine.simulate_and_render(sites=5, total_time_fs=40.0)
        print("\n" + "="*50)
        print("  OPEN QUANTUM LINDBLAD DENSITY MATRIX LATTICE")
        print("="*50)
        for row in res['ascii_quantum_matrix']:
            print("   " + row)
        print("="*50)
        print(f" • Site Populations: {res['final_site_populations']}\n • Final Cross-Coherence |rho_01|: {res['final_cross_coherence']}\n")
        return

    if args.fractal_turing:
        res = FractalTuringMorphogenesisEngine.render_fractal_tissue(grid_size=24, iterations=90)
        print("\n" + "="*50)
        print("  2D FRACTAL-BOUNDARY TURING TISSUE LATTICE")
        print("="*50)
        for line in res['fractal_ascii_tissue']:
            print("  " + line)
        print("="*50)
        print(f" • Fractal Coverage: {res['fractal_coverage_pct']} | Mean Activator: {res['mean_activator']}\n")
        return

    if args.origami_axes:
        res = MultiAxisOrigamiTorsionEngine.calculate_multi_axis_strain(args.origami_axes[0], args.origami_axes[1], args.origami_axes[2], args.origami_axes[3])
        print(f"\n • Multi-Axis Origami: {res['scaffold_bases']} bp ({res['spatial_axes']} Axes, {res['flexible_hinges']} Hinges)\n • Crossovers: {res['optimal_crossovers']} | Torsion Strain: {res['torsion_energy_pN_nm']} pN·nm ({res['mechanical_profile']})\n")
        return

    if args.deep_chrono:
        res = DeepChronomorphicShannonEngine.simulate_deep_decay(generations=args.deep_chrono[0])
        print(f"\n • Deep Chronomorphic Shannon: Retained = {res['final_retained_entropy']} bits (Loss: {res['information_loss_pct']})\n • Trajectory: {res['temporal_trajectory']}\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
