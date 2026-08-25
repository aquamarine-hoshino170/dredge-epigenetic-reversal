import argparse
import sys
import unittest
from dredge.bio_kernel import (
    HodgkinHuxleyCompartmentalEngine,
    QuantumFMOExcitonEngine,
    TuringMorphogenesisEngine,
    DNAOrigamiScaffoldEngine,
    ChronomorphicShannonEntropyEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Quantum-Coherent & Neuromorphic Suite (v55.0.0)')
    parser.add_argument('--hh-cable', action='store_true', help='Run Multi-Compartment Hodgkin-Huxley Cable PDE Simulation')
    parser.add_argument('--fmo-quantum', action='store_true', help='Simulate Quantum FMO Complex Exciton Coherence Dynamics')
    parser.add_argument('--turing-pattern', action='store_true', help='Render Turing Morphogenesis 2D Reaction-Diffusion Lattice')
    parser.add_argument('--origami-strain', nargs=2, type=int, metavar=('SCAFFOLD_BP', 'STAPLES'), help='Calculate 3D DNA Origami Torsion Strain')
    parser.add_argument('--chrono-entropy', nargs=1, type=int, metavar=('GENERATIONS',), help='Predict Epigenetic Shannon Manifold Decay')
    parser.add_argument('--test', action='store_true', help='Run Tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.hh_cable:
        res = HodgkinHuxleyCompartmentalEngine.simulate_axon_cable(compartments=8, total_time_ms=3.0)
        print(f"\n • Hodgkin-Huxley Cable: Soma V={res['final_soma_voltage']} mV | Terminal V={res['final_terminal_voltage']} mV\n • Propagation Sample:\n   {res['sampled_voltage_propagation']}\n")
        return

    if args.fmo_quantum:
        res = QuantumFMOExcitonEngine.simulate_coherence_dynamics(steps=40)
        print(f"\n • Quantum FMO Master Step: Site 1 Pop={res['site_1_population']}, Site 2={res['site_2_population']}, Site 3={res['site_3_population']}\n • Final Coherence |rho_12|: {res['final_off_diagonal_coherence']}\n")
        return

    if args.turing_pattern:
        res = TuringMorphogenesisEngine.render_turing_tissue(grid_size=20, iterations=100)
        print("\n" + "="*45)
        print("  TURING REACTION-DIFFUSION 2D LATTICE")
        print("="*45)
        for row in res['ascii_visual']:
            print("  " + row)
        print("="*45)
        print(f" • Pattern Type: {res['pattern_type']} | Mean Density: {res['mean_activator_density']}\n")
        return

    if args.origami_strain:
        res = DNAOrigamiScaffoldEngine.calculate_origami_torsion(args.origami_strain[0], args.origami_strain[1])
        print(f"\n • DNA Origami: {res['scaffold_bases']}bp | Twist: {res['accumulated_twist_degrees']}° | Torsion Energy: {res['torsional_strain_energy_pN_nm']} pN·nm ({res['structural_verdict']})\n")
        return

    if args.chrono_entropy:
        res = ChronomorphicShannonEntropyEngine.simulate_entropy_manifold(generations=args.chrono_entropy[0])
        print(f"\n • Chronomorphic Epigenetic Decay: Retained Entropy = {res['final_retained_entropy']} bits (Loss: {res['entropy_loss_pct']})\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
