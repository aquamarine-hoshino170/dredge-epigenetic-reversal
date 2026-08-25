import argparse
import sys
import numpy as np
from dredge.shell import start_interactive_shell
from dredge.bio_kernel import (
    UniversalBioKernel, 
    SequenceAlignmentEngine, 
    MolecularDockingEngine, 
    PharmacologyScreener, 
    ClinicalDiagnosticEngine, 
    NovelDiseaseDiscoveryEngine,
    SyntheticBiologyCircuit, 
    EpidemiologicalViralEngine, 
    GenerativeProteinDesigner,
    SyntheticLifeGenesisEngine, 
    TelomereLongevityEngine, 
    RNAFoldingLatticeEngine,
    MonoclonalAntibodyDesigner, 
    HodgkinHuxleyNeuronSimulator, 
    QuantumBiologyEngine,
    PhylogeneticEvolutionEngine, 
    MitochondrialBioenergeticsEngine, 
    BioSpectralVisualizer,
    BioFileIOAndMotifEngine, 
    DNADigitalStorageCodec,
    GoldenRatioBioGeometryEngine,
    XenobiologyAlienGeneticEngine,
    TuringMorphogenesisEngine,
    DNAOrigamiNanorobotEngine,
    EpigeneticShannonInformationEngine,
    ValportugiecResonatorEngine,
    PrigogineBioThermodynamicsEngine,
    CRISPRCas13DiagnosticEngine,
    CircadianClockOscillationEngine,
    LucasRuthlessQCEngine,
    ChronosHolographicMemoryEngine,
    BioVirtualMachineKernel,
    ApexRingZeroBioKernel,
    NativeAssemblyBitKernel
)

def main():
    if len(sys.argv) == 1:
        start_interactive_shell()
        return

    parser = argparse.ArgumentParser(
        prog="aquamarine-dredge",
        description="DREDGE Sovereign Ultra (v23.0.0): Hardware-Accelerated Universal Biological OS"
    )
    parser.add_argument("--version", action="version", version="aquamarine-dredge 23.0.0")
    
    # Ultra-Fast Hardware Flag
    parser.add_argument("--turbo-scan", type=str, default=None, help="Run 2-Bit Low-Level Assembly/Rust-Grade Hardware Scan on DNA")

    # Core Systems
    parser.add_argument("--kernel-irq", type=int, default=None, help="Trigger Hardware Bio-Interrupt")
    parser.add_argument("--payload", type=str, default="TET2_CpG_OVERLOAD", help="Interrupt payload")
    parser.add_argument("--exec-vm", nargs="+", help="Execute Bio-ISA bytecode")
    parser.add_argument("--atp", type=int, default=500, help="Initial ATP budget")
    parser.add_argument("--hologram", type=str, default=None, help="Holographic memory recall")
    parser.add_argument("--yamanaka", type=float, default=None, help="Yamanaka OSKM Reversal")
    parser.add_argument("--lucas", type=str, default=None, help="Trigger Lucas Angry Reaper")
    parser.add_argument("--thermo", action="store_true", help="Prigogine Thermodynamics")
    parser.add_argument("--cas13", type=str, default=None, help="CRISPR-Cas13 Sensor")
    parser.add_argument("--circadian", type=float, default=14.0, help="Circadian Oscillator")
    parser.add_argument("--valportugiec", type=str, default=None, help="Valportugiec Resonance")
    parser.add_argument("--infinity", action="store_true", help="Run Master Kernel")
    parser.add_argument("--cite", action="store_true", help="Print BibTeX citation")

    args = parser.parse_args()

    if args.turbo_scan:
        res = NativeAssemblyBitKernel.ultra_fast_bit_scan(args.turbo_scan)
        print("\n" + "="*76)
        print("  ⚡ NATIVE HARDWARE ACCELERATOR: 2-BIT ASSEMBLY/RUST PIPELINE")
        print("="*76)
        print(f" • Architecture Mode   : {res['hardware_mode']}")
        print(f" • Sequence Processed  : {res['sequence_length_nt']} Nucleotides")
        print(f" • 64-bit CPU Words    : {res['dense_64bit_registers_allocated']} Registers")
        print(f" • Execution Latency   : {res['execution_latency']}")
        print(f" • Peak Throughput     : {res['processing_throughput']}")
        print(f" • Memory Optimization : {res['memory_footprint_reduction']}")
        print(f" • GC Stability        : {res['gc_content']}")
        print("="*76 + "\n")
        return

    if args.kernel_irq is not None:
        res = ApexRingZeroBioKernel.trigger_kernel_interrupt(irq_code=args.kernel_irq, payload_data=args.payload)
        print(f"\n • Ring-0 Interrupt: {res['irq_vector_tripped']} | Status: {res['kernel_status']}\n")
        return

    if args.infinity:
        print("\n" + "="*76)
        print("  ♾️ AQUAMARINE DREDGE: GRAND SOVEREIGN ULTRA HEALTH & SPECTRUM")
        print("="*76)
        q_res = QuantumBiologyEngine.simulate_quantum_fmo_transfer()
        print(f" • [Quantum Biology]  : FMO Coherence Efficiency = {q_res['quantum_exciton_efficiency']}")
        n_res = HodgkinHuxleyNeuronSimulator.simulate_action_potential(12.0)
        print(f" • [Neuro-Physics]    : Action Potential Firing = {n_res['firing_frequency_Hz']}")
        dummy_wave = [np.sin(x/3.0) + np.cos(x/2.0) + 2.0 for x in range(50)]
        print(BioSpectralVisualizer.render_ascii_spectrum(dummy_wave, title="SOVEREIGN ULTRA SPECTRUM"))
        print("="*76 + "\n")
        return

    if args.cite:
        print("""@software{aquamarine_dredge_2026,
  author = {Hoshino, Aquamarine},
  title = {DREDGE Sovereign Ultra: Hardware-Accelerated Universal Biological OS},
  year = {2026},
  url = {https://pypi.org/project/aquamarine-dredge/}
}""")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
