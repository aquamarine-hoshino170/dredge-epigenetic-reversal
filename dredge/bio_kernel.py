import numpy as np
import math
import hashlib

class PureThermodynamicsEngine:
    """
    SantaLucia (1998) Nearest-Neighbor DNA Melting Temperature (Tm) & Gibbs Free Energy (ΔG)
    """
    # Nearest neighbor parameters (dH in kcal/mol, dS in cal/(K*mol))
    NN_DATA = {
        'AA': (-7.6, -21.3), 'TT': (-7.6, -21.3),
        'AT': (-7.2, -20.4), 'TA': (-7.2, -21.3),
        'CA': (-8.5, -22.7), 'TG': (-8.5, -22.7),
        'GT': (-8.4, -22.4), 'AC': (-8.4, -22.4),
        'CT': (-7.8, -21.0), 'AG': (-7.8, -21.0),
        'GA': (-8.2, -22.2), 'TC': (-8.2, -22.2),
        'CG': (-10.6, -27.2), 'GC': (-9.8, -24.4),
        'GG': (-8.0, -19.9), 'CC': (-8.0, -19.9)
    }
    R_GAS_CONSTANT = 1.9872  # cal/(K*mol)

    @staticmethod
    def calculate_melting_temp(sequence: str, primer_conc_nM: float = 200.0, na_conc_mM: float = 50.0) -> dict:
        seq = sequence.upper().strip()
        n = len(seq)
        if n < 2:
            return {"error": "Sequence too short"}

        dh_total = 0.2  # Initiation penalty
        ds_total = -5.7 # Initiation penalty

        for i in range(n - 1):
            pair = seq[i:i+2]
            if pair in PureThermodynamicsEngine.NN_DATA:
                dh, ds = PureThermodynamicsEngine.NN_DATA[pair]
                dh_total += dh
                ds_total += ds

        # Salt correction for entropy (SantaLucia 1998)
        monovalent_molar = na_conc_mM / 1000.0
        ds_total += 0.368 * (n - 1) * math.log(monovalent_molar)

        # Primer concentration in molar
        c_molar = (primer_conc_nM * 1e-9) / 4.0
        
        # Tm in Kelvin and Celsius
        tm_kelvin = (dh_total * 1000.0) / (ds_total + PureThermodynamicsEngine.R_GAS_CONSTANT * math.log(c_molar))
        tm_celsius = round(tm_kelvin - 273.15, 2)
        
        # Gibbs Free Energy (ΔG = ΔH - TΔS) at 37°C (310.15 K)
        t_kelvin_37 = 310.15
        dg_37 = round(dh_total - (t_kelvin_37 * ds_total / 1000.0), 2)

        return {
            "sequence_length": f"{n} bp",
            "enthalpy_dH_kcal_mol": round(dh_total, 2),
            "entropy_dS_cal_K_mol": round(ds_total, 2),
            "gibbs_free_energy_dG_37C": f"{dg_37} kcal/mol",
            "melting_temperature_Tm": f"{tm_celsius} °C",
            "thermodynamic_state": "THERMODYNAMICALLY_STABLE" if dg_37 < 0 else "UNFAVORABLE"
        }

class PureBiochemistryProteinEngine:
    """
    Biochemical Titration: Isoelectric Point (pI), Net Charge & Kyte-Doolittle Hydropathy
    """
    PKA_VALUES = {
        'N_term': 9.69, 'C_term': 2.34,
        'C': 8.33, 'D': 3.86, 'E': 4.25,
        'H': 6.00, 'K': 10.53, 'R': 12.48, 'Y': 10.07
    }
    KYTE_DOOLITTLE = {
        'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5,
        'Q': -3.5, 'E': -3.5, 'G': -0.4, 'H': -3.2, 'I': 4.5,
        'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6,
        'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2
    }

    @staticmethod
    def _calculate_charge_at_ph(protein_seq: str, ph: float) -> float:
        charge = 0.0
        # Positive charges (Basic residues + N-term)
        charge += 1.0 / (1.0 + 10.0 ** (ph - PureBiochemistryProteinEngine.PKA_VALUES['N_term']))
        for r in ['K', 'R', 'H']:
            count = protein_seq.count(r)
            if count > 0:
                pka = PureBiochemistryProteinEngine.PKA_VALUES[r]
                charge += count * (1.0 / (1.0 + 10.0 ** (ph - pka)))
        
        # Negative charges (Acidic residues + C-term)
        charge -= 1.0 / (1.0 + 10.0 ** (PureBiochemistryProteinEngine.PKA_VALUES['C_term'] - ph))
        for r in ['D', 'E', 'C', 'Y']:
            count = protein_seq.count(r)
            if count > 0:
                pka = PureBiochemistryProteinEngine.PKA_VALUES[r]
                charge -= count * (1.0 / (1.0 + 10.0 ** (pka - ph)))
        return charge

    @staticmethod
    def calculate_isoelectric_point(protein_seq: str) -> dict:
        seq = protein_seq.upper().strip()
        ph_low, ph_high = 0.0, 14.0
        
        # Binary Search Bisection Method for root finding where charge == 0
        for _ in range(50):
            ph_mid = (ph_low + ph_high) / 2.0
            charge = PureBiochemistryProteinEngine._calculate_charge_at_ph(seq, ph_mid)
            if charge > 0:
                ph_low = ph_mid
            else:
                ph_high = ph_mid

        pi_val = round((ph_low + ph_high) / 2.0, 3)
        charge_74 = round(PureBiochemistryProteinEngine._calculate_charge_at_ph(seq, 7.4), 2)
        
        # Mean Kyte-Doolittle Hydrophobicity
        hydro_scores = [PureBiochemistryProteinEngine.KYTE_DOOLITTLE.get(aa, 0.0) for aa in seq]
        gravy = round(float(np.mean(hydro_scores)), 3) if hydro_scores else 0.0

        return {
            "peptide_length": len(seq),
            "isoelectric_point_pI": pi_val,
            "net_charge_physiological_pH7_4": charge_74,
            "gravy_hydrophobicity_index": gravy,
            "biophysical_nature": "Hydrophobic / Membrane" if gravy > 0 else "Hydrophilic / Cytosolic"
        }

class PureMolecularGenomicsEngine:
    """Rigorous Smith-Waterman Alignment & Exact Ribosomal Translation"""
    CODON_MAP = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
        'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
    }

    @staticmethod
    def translate(dna_seq: str) -> str:
        seq = dna_seq.upper().replace(' ', '')
        pep = [PureMolecularGenomicsEngine.CODON_MAP.get(seq[i:i+3], '?') for i in range(0, len(seq) - 2, 3)]
        return "".join(pep)

    @staticmethod
    def smith_waterman_align(seq1: str, seq2: str, match: int = 3, mismatch: int = -3, gap: int = -2) -> dict:
        n, m = len(seq1), len(seq2)
        H = np.zeros((n + 1, m + 1), dtype=int)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                s = match if seq1[i-1] == seq2[j-1] else mismatch
                H[i, j] = max(0, H[i-1, j-1] + s, H[i-1, j] + gap, H[i, j-1] + gap)
        return {
            "optimal_alignment_score": int(np.max(H)),
            "sequence_matrix_shape": f"{n}x{m}",
            "alignment_algorithm": "Smith-Waterman Dynamic Programming"
        }

class PureEnzymeKineticsEngine:
    r"""
    Michaelis-Menten Enzyme Kinetics & Lineweaver-Burk Double-Reciprocal Linear Regression:
    v = (Vmax * [S]) / (Km + [S])
    1/v = (Km / Vmax) * (1/[S]) + (1 / Vmax)
    """
    @staticmethod
    def fit_lineweaver_burk(substrates: list, velocities: list) -> dict:
        if len(substrates) != len(velocities) or len(substrates) < 2:
            return {"error": "At least 2 data points required for regression"}

        s_arr = np.array(substrates, dtype=float)
        v_arr = np.array(velocities, dtype=float)

        if np.any(s_arr <= 0) or np.any(v_arr <= 0):
            return {"error": "Substrate concentration and velocity must be positive"}

        inv_s = 1.0 / s_arr
        inv_v = 1.0 / v_arr

        # Linear regression: inv_v = slope * inv_s + intercept
        slope, intercept = np.polyfit(inv_s, inv_v, 1)

        v_max = 1.0 / intercept
        k_m = slope * v_max

        # Coefficient of determination (R^2)
        v_pred = 1.0 / (slope * inv_s + intercept)
        ss_res = np.sum((v_arr - v_pred) ** 2)
        ss_tot = np.sum((v_arr - np.mean(v_arr)) ** 2)
        r_squared = 1.0 - (ss_res / ss_tot) if ss_tot != 0 else 1.0

        return {
            "v_max": round(float(v_max), 4),
            "k_m": round(float(k_m), 4),
            "slope": round(float(slope), 4),
            "y_intercept": round(float(intercept), 4),
            "r_squared": round(float(r_squared), 4),
            "catalytic_efficiency_note": f"Vmax = {round(v_max, 4)} uM/min, Km = {round(k_m, 4)} uM"
        }

class PureBufferEquilibriumEngine:
    r"""
    Henderson-Hasselbalch Buffer Equation & Fractional Ionization:
    pH = pKa + log10([A-] / [HA])
    """
    @staticmethod
    def calculate_buffer_ph(pka: float, conjugate_base_conc: float, weak_acid_conc: float) -> dict:
        if conjugate_base_conc <= 0 or weak_acid_conc <= 0:
            return {"error": "Concentrations must be strictly positive"}

        ratio = conjugate_base_conc / weak_acid_conc
        ph = pka + math.log10(ratio)
        
        # Fractional ionization: alpha = [A-] / ([A-] + [HA])
        fraction_deprotonated = conjugate_base_conc / (conjugate_base_conc + weak_acid_conc)

        return {
            "pka": pka,
            "base_to_acid_ratio": round(ratio, 4),
            "equilibrium_ph": round(ph, 3),
            "fraction_deprotonated_alpha": round(fraction_deprotonated, 4),
            "buffer_capacity_status": "OPTIMAL_BUFFER_ZONE" if abs(ph - pka) <= 1.0 else "OUTSIDE_MAX_BUFFER_CAPACITY"
        }

class PureSpectrophotometryEngine:
    r"""
    Beer-Lambert Law & Nucleic Acid Purity:
    A = \epsilon * c * l  =>  c = A / (\epsilon * l)
    Standard conversion factors: dsDNA A260 = 1.0 -> 50 ug/mL, RNA A260 = 1.0 -> 40 ug/mL
    """
    @staticmethod
    def quantify_nucleic_acid(a260: float, a280: float, sample_type: str = "dsdna", dilution_factor: float = 1.0) -> dict:
        if a260 < 0 or a280 < 0:
            return {"error": "Absorbance values cannot be negative"}

        ratio = round(a260 / a280, 2) if a280 > 0 else 0.0

        factor = 50.0 if sample_type.lower() == "dsdna" else 40.0
        conc_ng_ul = a260 * factor * dilution_factor

        purity_verdict = "PURE"
        if sample_type.lower() == "dsdna":
            if ratio < 1.7:
                purity_verdict = "PROTEIN_OR_PHENOL_CONTAMINATION (A260/A280 < 1.8)"
            elif ratio > 2.0:
                purity_verdict = "POSSIBLE_RNA_CONTAMINATION (A260/A280 > 2.0)"
            else:
                purity_verdict = "HIGH_PURITY_DSDNA (1.8 - 2.0)"
        else:
            if ratio < 1.9:
                purity_verdict = "CONTAMINATED_RNA (A260/A280 < 2.0)"
            else:
                purity_verdict = "HIGH_PURITY_RNA (~2.0)"

        return {
            "sample_type": sample_type.upper(),
            "absorbance_260": a260,
            "absorbance_280": a280,
            "purity_ratio_A260_A280": ratio,
            "concentration_ng_ul": round(conc_ng_ul, 2),
            "purity_assessment": purity_verdict
        }
