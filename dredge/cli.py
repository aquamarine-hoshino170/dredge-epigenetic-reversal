import argparse
import sys
import unittest
from dredge.bio_kernel import (
    BioConsensusBlockchainEngine,
    QuantumLindbladMasterEngine,
    TuringMorphogenesisEngine,
    DNAOrigamiTorsionEngine,
    HyperLatticeShannonEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Cloud-Smashing Bio-Operating Core (v56.0.0)')
    parser.add_argument('--bio-chain', nargs='+', help='Create Bio-Blockchain: --bio-chain MUT_A12G MUT_C34T')
    parser.add_argument('--quantum-fmo', action='store_true', help='Run Multi-Site Quantum Lindblad Solver')
    parser.add_argument('--turing-tissue', action='store_true', help='Render 2D Turing Morphogenesis Reaction Lattice')
    parser.add_argument('--origami-router', nargs=2, type=int, metavar=('SCAFFOLD', 'STAPLES'), help='3D DNA Origami Torsion Strain')
    parser.add_argument('--hyper-shannon', nargs=1, type=int, metavar=('GENERATIONS',), help='Hyper-Lattice Epigenetic Shannon Decay')
    parser.add_argument('--test', action='store_true', help='Run unit tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.bio_chain:
        blocks = BioConsensusBlockchainEngine.simulate_p2p_bio_chain(args.bio_chain)
        print("\n" + "="*55)
        print("  DECENTRALIZED PROOF-OF-SEQUENCE BIO-BLOCKCHAIN")
        print("="*55)
        for b in blocks:
            print(f" Block #{b['index']} | Data: {b['genomic_data']} | Hash: {b['block_hash'][:16]}... | Nonce: {b['nonce']}")
        print("="*55 + "\n")
        return

    if args.quantum_fmo:
        res = QuantumLindbladMasterEngine.simulate_fmo_lattice(sites=4, total_time_fs=50.0)
        print(f"\n • Quantum FMO Lattice ({res['total_sites']} Sites): Populations = {res['site_exciton_populations']} | Coherence = {res['final_cross_coherence']}\n")
        return

    if args.turing_tissue:
        res = TuringMorphogenesisEngine.generate_patterns(grid_size=20, iterations=100)
        print("\n" + "="*45)
        print("  2D TURING MORPHOGENESIS TISSUE RENDER")
        print("="*45)
        for r in res['ascii_render']:
            print("  " + r)
        print("="*45)
        print(f" • Mean Activator Density: {res['mean_activator_concentration']}\n")
        return

    if args.origami_router:
        res = DNAOrigamiTorsionEngine.calculate_torsion(args.origami_router[0], args.origami_router[1])
        print(f"\n • DNA Origami: {res['scaffold_length']} | Crossovers: {res['crossover_junctions']} | Strain: {res['torsion_energy_pN_nm']} pN·nm ({res['structural_stability']})\n")
        return

    if args.hyper_shannon:
        res = HyperLatticeShannonEngine.simulate_decay(generations=args.hyper_shannon[0])
        print(f"\n • Epigenetic Shannon Decay: Retained = {res['final_retained_entropy']} bits (Loss: {res['entropy_loss_percentage']})\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
