import numpy as np
import math
import random

class QuantumMolecularDockingEngine:
    r"""
    Empirical Binding Free Energy & Hybrid Potential Model
    dG_bind = dG_vdW + dG_elec + dG_hbond + dG_tor
    """
    @staticmethod
    def calculate_binding_affinity(num_heavy_atoms: int = 15, rotatable_bonds: int = 4, contact_distance_angstrom: float = 2.8) -> dict:
        r = max(1.5, contact_distance_angstrom)
        
        # Lennard-Jones 12-6 Potential (vdW)
        A, B = 1e5, 1e3
        vdw_energy = (A / (r**12)) - (B / (r**6))
        
        # Electrostatic Screened Coulombic Potential (dielectric constant eps(r) = 4r)
        q1, q2 = 0.4, -0.4
        coulombic_energy = (332.0 * q1 * q2) / (4.0 * (r**2))
        
        # Hydrogen bonding 12-10 potential
        hbond_energy = -2.5 * math.exp(-((r - 2.8)**2) / 0.2)
        
        # Torsional conformational entropy loss penalty
        torsion_penalty = 0.31 * rotatable_bonds # kcal/mol per rotatable bond
        
        dg_total = round(vdw_energy + coulombic_energy + hbond_energy + torsion_penalty, 3)
        
        # Dissociation Constant: Kd = exp(dG / RT) at 298.15K (RT = 0.592 kcal/mol)
        rt = 0.592
        kd_molar = math.exp(dg_total / rt)
        
        if kd_molar < 1e-6:
            kd_str = f"{round(kd_molar * 1e9, 2)} nM"
        elif kd_molar < 1e-3:
            kd_str = f"{round(kd_molar * 1e6, 2)} uM"
        else:
            kd_str = f"{round(kd_molar * 1e3, 2)} mM"

        return {
            "contact_distance_A": r,
            "vdw_potential_kcal_mol": round(vdw_energy, 3),
            "electrostatic_potential_kcal_mol": round(coulombic_energy, 3),
            "hbond_energy_kcal_mol": round(hbond_energy, 3),
            "torsion_entropy_penalty_kcal_mol": round(torsion_penalty, 3),
            "total_binding_free_energy_dG": f"{dg_total} kcal/mol",
            "predicted_dissociation_constant_Kd": kd_str,
            "affinity_class": "HIGH_AFFINITY_DRUG_CANDIDATE" if dg_total < -7.0 else "MODERATE_OR_WEAK_BINDER"
        }

class DirectedEvolutionDAGEngine:
    r"""
    Directed Acyclic Graph (DAG) Evolutionary Lineage & Fitness Trajectory
    """
    @staticmethod
    def simulate_evolution(generations: int = 5, population_size: int = 4, mutation_rate: float = 0.15) -> dict:
        nodes = {}
        lineage_tree = []
        
        # Root sequence
        current_pop = [{"id": f"G0_M{i}", "seq": "ATGCGATCGCTA", "fitness": 1.0} for i in range(population_size)]
        
        for g in range(1, generations + 1):
            next_pop = []
            for i, parent in enumerate(current_pop):
                child_seq = list(parent["seq"])
                mutated = False
                for idx in range(len(child_seq)):
                    if random.random() < mutation_rate:
                        child_seq[idx] = random.choice(['A', 'C', 'G', 'T'])
                        mutated = True
                
                # Fitness function: GC content and optimal motif proximity
                seq_str = "".join(child_seq)
                gc_ratio = (seq_str.count('G') + seq_str.count('C')) / len(seq_str)
                fitness_score = round(parent["fitness"] * (1.0 + (gc_ratio - 0.5) * 0.8), 3)
                
                child_id = f"G{g}_M{i}"
                child_node = {"id": child_id, "parent": parent["id"], "seq": seq_str, "fitness": fitness_score}
                next_pop.append(child_node)
                
                lineage_tree.append(f"  [{parent['id']} (fit:{parent['fitness']})] ──> [{child_id} (fit:{fitness_score}) | {seq_str[:6]}...]")
            current_pop = next_pop

        best_variant = max(current_pop, key=lambda x: x["fitness"])

        return {
            "total_generations": generations,
            "final_population_count": len(current_pop),
            "top_fitness_score": best_variant["fitness"],
            "top_evolved_sequence": best_variant["seq"],
            "lineage_dag_ascii": lineage_tree[:10]
        }

class NonNewtonianVascularEngine:
    r"""
    Non-Newtonian Blood Hemodynamics (Casson Fluid Capillary Shear & Pressure Gradient)
    """
    @staticmethod
    def calculate_hemodynamics(vessel_radius_um: float = 15.0, flow_rate_nl_s: float = 2.5, hematocrit: float = 0.45) -> dict:
        r_m = vessel_radius_um * 1e-6
        q_m3_s = flow_rate_nl_s * 1e-12
        
        # Casson yield stress for blood (function of hematocrit)
        tau_yield = 0.005 * (hematocrit ** 3) # Pa
        plasma_viscosity = 0.0012 # Pa*s
        
        # Poiseuille base shear rate: gamma_dot = 4 * Q / (pi * R^3)
        shear_rate = (4.0 * q_m3_s) / (math.pi * (r_m ** 3))
        
        # Casson Apparent Viscosity: sqrt(tau) = sqrt(tau_y) + sqrt(mu * gamma_dot)
        wall_shear_stress = (math.sqrt(tau_yield) + math.sqrt(plasma_viscosity * shear_rate)) ** 2
        apparent_viscosity = wall_shear_stress / max(1e-6, shear_rate)
        
        # Pressure drop per millimeter length (dp/dx = 2 * tau_w / R)
        pressure_drop_pa_mm = (2.0 * wall_shear_stress / r_m) * 1e-3
        pressure_drop_mmhg_mm = pressure_drop_pa_mm * 0.00750062

        return {
            "vessel_radius": f"{vessel_radius_um} um",
            "wall_shear_rate_s1": round(float(shear_rate), 2),
            "wall_shear_stress_Pa": round(float(wall_shear_stress), 4),
            "apparent_blood_viscosity_cP": round(float(apparent_viscosity * 1000.0), 3),
            "pressure_gradient_mmHg_mm": round(float(pressure_drop_mmhg_mm), 3),
            "flow_regime": "LAMINAR_MICROVASCULAR_CAPILLARY" if shear_rate < 1000.0 else "HIGH_SHEAR_MICROCIRCULATION"
        }

class XenobiologyCircuitCompilerEngine:
    r"""
    Synthetic Xenobiology Compiler (Hachimoji 6-Letter DNA: A, T, G, C, P, Z)
    """
    HACHIMOJI_PAIRS = {
        'A': 'T', 'T': 'A',
        'G': 'C', 'C': 'G',
        'P': 'Z', 'Z': 'P'  # Non-standard synthetic letters (2-amino-8-(1'-beta-D-2'-deoxyribofuranosyl)-imidazo-[1,2-a]-1,3,5-triazin-4(8H)-one)
    }

    @staticmethod
    def compile_xeno_circuit(synthetic_seq: str, induction_level: float = 1.0) -> dict:
        seq = synthetic_seq.upper().strip()
        n = len(seq)
        
        # Synthesize complementary strand
        comp_strand = []
        synthetic_bases_count = 0
        for b in seq:
            if b in XenobiologyCircuitCompilerEngine.HACHIMOJI_PAIRS:
                comp_strand.append(XenobiologyCircuitCompilerEngine.HACHIMOJI_PAIRS[b])
                if b in ('P', 'Z'):
                    synthetic_bases_count += 1
            else:
                comp_strand.append('?')

        # Metabolic transcription load (Hill function logic: V = Vmax * I^n / (K^n + I^n))
        hill_n = 2.5
        k_m = 0.5
        promoter_activity = (induction_level ** hill_n) / ((k_m ** hill_n) + (induction_level ** hill_n))
        metabolic_tax = (synthetic_bases_count * 1.5) + (n * 0.1)
        
        signal_delay_ms = round(12.0 + (synthetic_bases_count * 2.4), 2)

        return {
            "xeno_sequence_length": f"{n} bp",
            "synthetic_hachimoji_bases": synthetic_bases_count,
            "complementary_xeno_strand": "".join(comp_strand),
            "promoter_transcription_efficiency": f"{round(promoter_activity * 100.0, 2)}%",
            "metabolic_chassis_burden_index": round(metabolic_tax, 2),
            "circuit_propagation_delay_ms": signal_delay_ms,
            "orthogonal_chassis_status": "HIGHLY_ORTHOGONAL_SYNTHETIC_CELL" if synthetic_bases_count >= 2 else "PARTIALLY_CANONICAL"
        }
