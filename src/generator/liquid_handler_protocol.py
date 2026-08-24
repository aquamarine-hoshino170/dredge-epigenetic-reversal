import os

def generate_opentrons_protocol(lead_id="DREDGE-05", num_replicates=3):
    """
    Generates an automated Opentrons OT-2 Python Protocol (API v2.13)
    for 96-well plate TET2 fluorometric demethylation screening assay.
    """
    protocol_script = f'''# ===============================================================
#       DREDGE Epigenetic Assay Automated Robot Protocol (OT-2)
# ===============================================================
# Protocol: 96-Well Plate High-Throughput TET2 Demethylation Screen
# Target: {lead_id} Rejuvenation Molecule Assay
# Generated automatically by DREDGE Robotic Lab Engine

from opentrons import protocol_api

metadata = {{
    "protocolName": "DREDGE TET2 Fluorometric Assay ({lead_id})",
    "author": "Aquamarine Hoshino",
    "description": "Automated serial dilution and dispensing for TET2 epigenetic screening",
    "apiLevel": "2.13"
}}

def run(protocol: protocol_api.ProtocolContext):
    # Labware Setup
    tiprack = protocol.load_labware("opentrons_96_tiprack_300ul", "1")
    plate_96 = protocol.load_labware("corning_96_wellplate_360ul_flat", "2")
    reagent_reservoir = protocol.load_labware("nest_12_reservoir_15ml", "3")
    
    # Pipette
    p300 = protocol.load_instrument("p300_single_gen2", "right", tip_racks=[tiprack])

    # Reagents definition in reservoir
    tet2_enzyme_buffer = reagent_reservoir.wells()[0]
    lead_stock_dredge05 = reagent_reservoir.wells()[1]
    methylated_dna_substrate = reagent_reservoir.wells()[2]
    detection_fluorophore = reagent_reservoir.wells()[3]

    protocol.comment("--- Dispensing 40uL TET2 Reaction Buffer across Assay Plate ---")
    p300.pick_up_tip()
    for col in plate_96.columns()[0:6]:
        for well in col:
            p300.aspirate(40, tet2_enzyme_buffer)
            p300.dispense(40, well)
    p300.drop_tip()

    protocol.comment("--- Performing Serial Dilution of Lead Molecule ({lead_id}) ---")
    p300.pick_up_tip()
    p300.aspirate(60, lead_stock_dredge05)
    p300.dispense(60, plate_96.columns()[0][0])
    
    for i in range(len(plate_96.columns()[0]) - 1):
        source = plate_96.columns()[0][i]
        target = plate_96.columns()[0][i+1]
        p300.aspirate(30, source)
        p300.dispense(30, target)
        p300.mix(3, 20, target)
    p300.drop_tip()

    protocol.comment("--- Dispensing Fluorogenic Methylated Substrate ---")
    p300.pick_up_tip()
    for col in plate_96.columns()[0:6]:
        for well in col:
            p300.aspirate(10, methylated_dna_substrate)
            p300.dispense(10, well)
    p300.drop_tip()

    protocol.comment("--- Plate Ready for 37°C 60-min Epigenetic Incubation & Plate Reader ---")
'''
    return protocol_script

def run_lab_automation_pipeline():
    print("===============================================================")
    print("    DREDGE Automated Wet-Lab Robotic Protocol Generator       ")
    print("===============================================================")
    print("Target Standard: Opentrons OT-2 API v2.13 | 96-Well Microplate")
    print("Assay: In-vitro TET2 Fluorometric Epigenetic Demethylation")
    print("---------------------------------------------------------------\n")

    protocol_code = generate_opentrons_protocol("DREDGE-05")

    os.makedirs("data/processed/lab_automation", exist_ok=True)
    out_py = "data/processed/lab_automation/ot2_tet2_assay_protocol.py"

    with open(out_py, "w", encoding="utf-8") as f:
        f.write(protocol_code)

    print(f"  • Labware Deck Config   : 96-Well Flat Bottom + 12-Channel Reservoir")
    print(f"  • Pipette Channel       : P300 Single-Channel Gen2")
    print(f"  • Assay Steps Automated : Buffer dispensing, serial dilution, substrate addition")
    print(f"  • Incubation Requirement: 37°C for 60 mins under plate reader")
    print("-" * 65)
    print(f"[✓] Automated pipetting protocol generated successfully: {out_py}\n")

if __name__ == "__main__":
    run_lab_automation_pipeline()
