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

class FastqQualityFilterEngine:
    r"""
    Fastq Phred Quality Score Engine:
    Q = -10 * log10(P_error)
    ASCII Sanger Phred+33 offset decoding: Q = ord(char) - 33
    """
    @staticmethod
    def parse_phred_scores(qual_str: str, phred_offset: int = 33) -> list:
        return [ord(c) - phred_offset for c in qual_str.strip()]

    @staticmethod
    def filter_read(seq: str, qual_str: str, min_q: float = 20.0, max_low_q_fraction: float = 0.1) -> dict:
        seq = seq.strip()
        qual_str = qual_str.strip()
        if len(seq) != len(qual_str) or len(seq) == 0:
            return {"error": "Sequence and quality string length mismatch"}

        scores = [ord(c) - 33 for c in qual_str]
        mean_q = round(float(np.mean(scores)), 2)
        low_q_count = sum(1 for q in scores if q < min_q)
        low_q_fraction = round(low_q_count / len(scores), 4)
        
        # Mean error probability: P = 10^(-Q/10)
        mean_p_error = round(float(np.mean([10.0 ** (-q / 10.0) for q in scores])), 6)
        is_pass = (mean_q >= min_q) and (low_q_fraction <= max_low_q_fraction)

        return {
            "read_length": len(seq),
            "mean_phred_score": mean_q,
            "mean_error_probability": mean_p_error,
            "low_quality_bases_pct": round(low_q_fraction * 100, 2),
            "quality_filter_status": "PASS" if is_pass else "FAIL",
            "accuracy_confidence": f"{round((1.0 - mean_p_error) * 100, 4)}%"
        }

class PopulationGeneticsEngine:
    r"""
    Hardy-Weinberg Equilibrium & Allele Frequencies:
    p + q = 1  =>  p^2 + 2pq + q^2 = 1
    Chi-Square Goodness-of-Fit Test for Equilibrium Deviation
    """
    @staticmethod
    def calculate_hardy_weinberg(obs_AA: int, obs_Aa: int, obs_aa: int) -> dict:
        total_ind = obs_AA + obs_Aa + obs_aa
        if total_ind <= 0:
            return {"error": "Total population must be greater than zero"}

        total_alleles = 2 * total_ind
        p = ((2 * obs_AA) + obs_Aa) / total_alleles
        q = 1.0 - p

        exp_AA = (p ** 2) * total_ind
        exp_Aa = (2 * p * q) * total_ind
        exp_aa = (q ** 2) * total_ind

        # Chi-Square Test (df = 1, critical value at alpha=0.05 is 3.841)
        chi2 = 0.0
        for obs, exp in zip([obs_AA, obs_Aa, obs_aa], [exp_AA, exp_Aa, exp_aa]):
            if exp > 0:
                chi2 += ((obs - exp) ** 2) / exp

        is_equilibrium = chi2 < 3.841

        return {
            "total_population": total_ind,
            "allele_frequency_p": round(p, 4),
            "allele_frequency_q": round(q, 4),
            "genotype_freq_AA_p2": round(p**2, 4),
            "genotype_freq_Aa_2pq": round(2*p*q, 4),
            "genotype_freq_aa_q2": round(q**2, 4),
            "chi_square_stat": round(chi2, 4),
            "equilibrium_status": "IN_HARDY_WEINBERG_EQUILIBRIUM" if is_equilibrium else "DEVIATES_FROM_EQUILIBRIUM"
        }

class RNASecondaryStructureEngine:
    r"""
    Nussinov Dynamic Programming Algorithm:
    Predicts maximum number of nested Watson-Crick & Wobble Base Pairs in RNA
    N(i, j) = max( N(i+1, j), N(i, j-1), N(i+1, j-1) + \delta(i, j), max_{i<=k<j}(N(i, k) + N(k+1, j)) )
    """
    CANONICAL_PAIRS = {('A', 'U'), ('U', 'A'), ('G', 'C'), ('C', 'G'), ('G', 'U'), ('U', 'G')}

    @staticmethod
    def nussinov_fold(rna_sequence: str, min_loop_len: int = 3) -> dict:
        seq = rna_sequence.upper().strip().replace('T', 'U')
        n = len(seq)
        if n < min_loop_len + 2:
            return {"error": "Sequence too short for RNA secondary structure"}

        DP = np.zeros((n, n), dtype=int)

        # Fill dynamic programming matrix along diagonals
        for length in range(min_loop_len + 1, n):
            for i in range(n - length):
                j = i + length
                # Case 1: Unpaired positions
                DP[i, j] = max(DP[i + 1, j], DP[i, j - 1])

                # Case 2: Base pair between i and j
                if (seq[i], seq[j]) in RNASecondaryStructureEngine.CANONICAL_PAIRS:
                    DP[i, j] = max(DP[i, j], DP[i + 1, j - 1] + 1)

                # Case 3: Bifurcation
                for k in range(i + 1, j):
                    DP[i, j] = max(DP[i, j], DP[i, k] + DP[k + 1, j])

        max_pairs = int(DP[0, n - 1])
        base_pair_density = round((2 * max_pairs / n) * 100, 2)

        return {
            "rna_length": f"{n} nt",
            "max_nested_base_pairs": max_pairs,
            "paired_nucleotide_pct": f"{base_pair_density}%",
            "structure_matrix_shape": f"{n}x{n}",
            "folding_model": "Nussinov Dynamic Matrix"
        }

class EnzymeInhibitionEngine:
    r"""
    Enzyme Inhibition Kinetics:
    Competitive: Km_app = Km * (1 + [I] / Ki), Vmax_app = Vmax
    Non-Competitive: Vmax_app = Vmax / (1 + [I] / Ki), Km_app = Km
    Uncompetitive: Vmax_app = Vmax / (1 + [I] / Ki), Km_app = Km / (1 + [I] / Ki)
    """
    @staticmethod
    def calculate_inhibition(v_max: float, k_m: float, inhibitor_conc: float, k_i: float, mode: str = "competitive") -> dict:
        if v_max <= 0 or k_m <= 0 or k_i <= 0 or inhibitor_conc < 0:
            return {"error": "Kinetic constants and concentrations must be positive"}

        alpha = 1.0 + (inhibitor_conc / k_i)
        mode = mode.lower().strip()

        if mode == "competitive":
            v_max_app = v_max
            k_m_app = k_m * alpha
        elif mode == "noncompetitive" or mode == "non-competitive":
            v_max_app = v_max / alpha
            k_m_app = k_m
        elif mode == "uncompetitive":
            v_max_app = v_max / alpha
            k_m_app = k_m / alpha
        else:
            return {"error": f"Unknown inhibition mode: {mode}"}

        # Apparent catalytic efficiency (Vmax_app / Km_app)
        eff_native = v_max / k_m
        eff_inhibited = v_max_app / k_m_app
        eff_drop = round((1.0 - (eff_inhibited / eff_native)) * 100, 2)

        return {
            "inhibition_mode": mode.upper(),
            "inhibitor_concentration": inhibitor_conc,
            "inhibition_factor_alpha": round(alpha, 4),
            "native_Vmax": v_max,
            "apparent_Vmax": round(v_max_app, 4),
            "native_Km": k_m,
            "apparent_Km": round(k_m_app, 4),
            "efficiency_loss": f"{eff_drop}%"
        }
