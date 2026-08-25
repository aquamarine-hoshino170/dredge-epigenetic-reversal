import numpy as np
import math
import hashlib

class PureThermodynamicsEngine:
    """SantaLucia (1998) Nearest-Neighbor DNA Melting Temperature (Tm) & Gibbs Free Energy (ΔG)"""
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
    R_GAS_CONSTANT = 1.9872

    @staticmethod
    def calculate_melting_temp(sequence: str, primer_conc_nM: float = 200.0, na_conc_mM: float = 50.0) -> dict:
        seq = sequence.upper().strip()
        n = len(seq)
        if n < 2:
            return {"error": "Sequence too short"}

        dh_total, ds_total = 0.2, -5.7
        for i in range(n - 1):
            pair = seq[i:i+2]
            if pair in PureThermodynamicsEngine.NN_DATA:
                dh, ds = PureThermodynamicsEngine.NN_DATA[pair]
                dh_total += dh
                ds_total += ds

        monovalent_molar = na_conc_mM / 1000.0
        ds_total += 0.368 * (n - 1) * math.log(monovalent_molar)
        c_molar = (primer_conc_nM * 1e-9) / 4.0
        
        tm_kelvin = (dh_total * 1000.0) / (ds_total + PureThermodynamicsEngine.R_GAS_CONSTANT * math.log(c_molar))
        tm_celsius = round(tm_kelvin - 273.15, 2)
        dg_37 = round(dh_total - (310.15 * ds_total / 1000.0), 2)

        return {
            "sequence_length": f"{n} bp",
            "enthalpy_dH_kcal_mol": round(dh_total, 2),
            "entropy_dS_cal_K_mol": round(ds_total, 2),
            "gibbs_free_energy_dG_37C": f"{dg_37} kcal/mol",
            "melting_temperature_Tm": f"{tm_celsius} °C",
            "thermodynamic_state": "THERMODYNAMICALLY_STABLE" if dg_37 < 0 else "UNFAVORABLE"
        }

class PureBiochemistryProteinEngine:
    """Biochemical Titration: Isoelectric Point (pI), Net Charge & Kyte-Doolittle Hydropathy"""
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
        charge = 1.0 / (1.0 + 10.0 ** (ph - PureBiochemistryProteinEngine.PKA_VALUES['N_term']))
        for r in ['K', 'R', 'H']:
            charge += protein_seq.count(r) * (1.0 / (1.0 + 10.0 ** (ph - PureBiochemistryProteinEngine.PKA_VALUES[r])))
        charge -= 1.0 / (1.0 + 10.0 ** (PureBiochemistryProteinEngine.PKA_VALUES['C_term'] - ph))
        for r in ['D', 'E', 'C', 'Y']:
            charge -= protein_seq.count(r) * (1.0 / (1.0 + 10.0 ** (PureBiochemistryProteinEngine.PKA_VALUES[r] - ph)))
        return charge

    @staticmethod
    def calculate_isoelectric_point(protein_seq: str) -> dict:
        seq = protein_seq.upper().strip()
        ph_low, ph_high = 0.0, 14.0
        for _ in range(50):
            ph_mid = (ph_low + ph_high) / 2.0
            if PureBiochemistryProteinEngine._calculate_charge_at_ph(seq, ph_mid) > 0:
                ph_low = ph_mid
            else:
                ph_high = ph_mid

        pi_val = round((ph_low + ph_high) / 2.0, 3)
        charge_74 = round(PureBiochemistryProteinEngine._calculate_charge_at_ph(seq, 7.4), 2)
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
    """Smith-Waterman Alignment & Exact Ribosomal Translation"""
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
    """Michaelis-Menten Kinetics & Lineweaver-Burk Linear Regression"""
    @staticmethod
    def fit_lineweaver_burk(substrates: list, velocities: list) -> dict:
        s_arr = np.array(substrates, dtype=float)
        v_arr = np.array(velocities, dtype=float)
        inv_s = 1.0 / s_arr
        inv_v = 1.0 / v_arr
        slope, intercept = np.polyfit(inv_s, inv_v, 1)
        v_max = 1.0 / intercept
        k_m = slope * v_max
        v_pred = 1.0 / (slope * inv_s + intercept)
        ss_res = np.sum((v_arr - v_pred) ** 2)
        ss_tot = np.sum((v_arr - np.mean(v_arr)) ** 2)
        r_squared = 1.0 - (ss_res / ss_tot) if ss_tot != 0 else 1.0
        return {
            "v_max": round(float(v_max), 4),
            "k_m": round(float(k_m), 4),
            "r_squared": round(float(r_squared), 4)
        }

class PureBufferEquilibriumEngine:
    """Henderson-Hasselbalch Buffer Equilibrium"""
    @staticmethod
    def calculate_buffer_ph(pka: float, conjugate_base_conc: float, weak_acid_conc: float) -> dict:
        ratio = conjugate_base_conc / weak_acid_conc
        ph = pka + math.log10(ratio)
        return {
            "pka": pka,
            "base_to_acid_ratio": round(ratio, 4),
            "equilibrium_ph": round(ph, 3),
            "buffer_capacity_status": "OPTIMAL_BUFFER_ZONE" if abs(ph - pka) <= 1.0 else "OUTSIDE_MAX_BUFFER_CAPACITY"
        }

class PureSpectrophotometryEngine:
    """Beer-Lambert Law & Nucleic Acid Purity"""
    @staticmethod
    def quantify_nucleic_acid(a260: float, a280: float, sample_type: str = "dsdna") -> dict:
        ratio = round(a260 / a280, 2) if a280 > 0 else 0.0
        factor = 50.0 if sample_type.lower() == "dsdna" else 40.0
        conc = a260 * factor
        purity = "HIGH_PURITY" if 1.8 <= ratio <= 2.0 else "POSSIBLE_CONTAMINATION"
        return {
            "sample_type": sample_type.upper(),
            "purity_ratio_A260_A280": ratio,
            "concentration_ng_ul": round(conc, 2),
            "purity_assessment": purity
        }

class BigDataGenomicsEngine:
    @staticmethod
    def burrows_wheeler_transform(sequence: str) -> dict:
        seq = sequence.upper().strip() + "$"
        rotations = sorted([seq[i:] + seq[:i] for i in range(len(seq))])
        bwt_str = "".join([r[-1] for r in rotations])
        return {
            'original_length': len(sequence),
            'bwt_transformed': bwt_str,
            'compression_readiness': f"{round((1.0 - len(set(bwt_str))/len(bwt_str))*100, 2)}% Entropy Density"
        }

    @staticmethod
    def needleman_wunsch_global_align(seq1: str, seq2: str, match: int = 1, mismatch: int = -1, gap: int = -1) -> dict:
        n, m = len(seq1), len(seq2)
        score_matrix = np.zeros((n + 1, m + 1), dtype=int)
        for i in range(n + 1): score_matrix[i][0] = i * gap
        for j in range(m + 1): score_matrix[0][j] = j * gap

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                s = match if seq1[i-1] == seq2[j-1] else mismatch
                score_matrix[i][j] = max(
                    score_matrix[i-1][j-1] + s,
                    score_matrix[i-1][j] + gap,
                    score_matrix[i][j-1] + gap
                )
        return {
            'global_alignment_score': int(score_matrix[n][m]),
            'alignment_dimensions': f'{n}x{m}',
            'algorithm': 'Needleman-Wunsch Dynamic Programming'
        }
