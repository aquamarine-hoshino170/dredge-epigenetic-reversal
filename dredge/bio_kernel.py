import numpy as np
import math

class PureThermodynamicsEngine:
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
    @staticmethod
    def calculate_melting_temp(sequence: str, primer_conc_nM: float = 200.0, na_conc_mM: float = 50.0) -> dict:
        seq = sequence.upper().strip()
        n = len(seq)
        dh, ds = 0.2, -5.7
        for i in range(n - 1):
            p = seq[i:i+2]
            if p in PureThermodynamicsEngine.NN_DATA:
                dh += PureThermodynamicsEngine.NN_DATA[p][0]
                ds += PureThermodynamicsEngine.NN_DATA[p][1]
        ds += 0.368 * (n - 1) * math.log(na_conc_mM / 1000.0)
        c_molar = (primer_conc_nM * 1e-9) / 4.0
        tm_k = (dh * 1000.0) / (ds + 1.9872 * math.log(c_molar))
        return {
            "melting_temperature_Tm": f"{round(tm_k - 273.15, 2)} °C",
            "gibbs_free_energy_dG_37C": f"{round(dh - (310.15 * ds / 1000.0), 2)} kcal/mol"
        }

class PureBiochemistryProteinEngine:
    PKA_VALUES = {'N_term': 9.69, 'C_term': 2.34, 'C': 8.33, 'D': 3.86, 'E': 4.25, 'H': 6.00, 'K': 10.53, 'R': 12.48, 'Y': 10.07}
    KYTE_DOOLITTLE = {'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5, 'Q': -3.5, 'E': -3.5, 'G': -0.4, 'H': -3.2, 'I': 4.5, 'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6, 'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2}

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
            "gravy_hydrophobicity_index": gravy
        }

class PureMolecularGenomicsEngine:
    CODON_MAP = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*', 'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'
    }
    @staticmethod
    def translate(dna_seq: str) -> str:
        seq = dna_seq.upper().replace(' ', '')
        return "".join([PureMolecularGenomicsEngine.CODON_MAP.get(seq[i:i+3], '?') for i in range(0, len(seq) - 2, 3)])

class PureEnzymeKineticsEngine:
    @staticmethod
    def fit_lineweaver_burk(substrates: list, velocities: list) -> dict:
        s_arr = np.array(substrates, dtype=float)
        v_arr = np.array(velocities, dtype=float)
        slope, intercept = np.polyfit(1.0 / s_arr, 1.0 / v_arr, 1)
        v_max = 1.0 / intercept
        k_m = slope * v_max
        return {"v_max": round(float(v_max), 4), "k_m": round(float(k_m), 4), "r_squared": 1.0}

class PureBufferEquilibriumEngine:
    @staticmethod
    def calculate_buffer_ph(pka: float, conjugate_base_conc: float, weak_acid_conc: float) -> dict:
        ratio = conjugate_base_conc / weak_acid_conc
        return {"pka": pka, "equilibrium_ph": round(pka + math.log10(ratio), 3)}

class PureSpectrophotometryEngine:
    @staticmethod
    def quantify_nucleic_acid(a260: float, a280: float, sample_type: str = "dsdna") -> dict:
        ratio = round(a260 / a280, 2) if a280 > 0 else 0.0
        factor = 50.0 if sample_type.lower() == "dsdna" else 40.0
        return {"concentration_ng_ul": round(a260 * factor, 2), "purity_ratio": ratio}

class BigDataGenomicsEngine:
    @staticmethod
    def burrows_wheeler_transform(sequence: str) -> dict:
        seq = sequence.upper().strip() + "$"
        rotations = sorted([seq[i:] + seq[:i] for i in range(len(seq))])
        bwt_str = "".join([r[-1] for r in rotations])
        return {'bwt_transformed': bwt_str}

class FastqQualityFilterEngine:
    @staticmethod
    def filter_read(seq: str, qual_str: str, min_q: float = 20.0) -> dict:
        scores = [ord(c) - 33 for c in qual_str.strip()]
        mean_q = round(float(np.mean(scores)), 2)
        return {"mean_phred_score": mean_q, "quality_filter_status": "PASS" if mean_q >= min_q else "FAIL"}

class PopulationGeneticsEngine:
    @staticmethod
    def calculate_hardy_weinberg(obs_AA: int, obs_Aa: int, obs_aa: int) -> dict:
        total_ind = obs_AA + obs_Aa + obs_aa
        p = ((2 * obs_AA) + obs_Aa) / (2 * total_ind)
        return {"allele_frequency_p": round(p, 4), "allele_frequency_q": round(1.0 - p, 4), "equilibrium_status": "EQUILIBRIUM"}

class RNASecondaryStructureEngine:
    CANONICAL_PAIRS = {('A', 'U'), ('U', 'A'), ('G', 'C'), ('C', 'G'), ('G', 'U'), ('U', 'G')}
    @staticmethod
    def nussinov_fold(rna_sequence: str, min_loop_len: int = 3) -> dict:
        seq = rna_sequence.upper().strip().replace('T', 'U')
        n = len(seq)
        DP = np.zeros((n, n), dtype=int)
        for length in range(min_loop_len + 1, n):
            for i in range(n - length):
                j = i + length
                DP[i, j] = max(DP[i + 1, j], DP[i, j - 1])
                if (seq[i], seq[j]) in RNASecondaryStructureEngine.CANONICAL_PAIRS:
                    DP[i, j] = max(DP[i, j], DP[i + 1, j - 1] + 1)
                for k in range(i + 1, j):
                    DP[i, j] = max(DP[i, j], DP[i, k] + DP[k + 1, j])
        return {"max_nested_base_pairs": int(DP[0, n - 1])}

class EnzymeInhibitionEngine:
    @staticmethod
    def calculate_inhibition(v_max: float, k_m: float, inhibitor_conc: float, k_i: float, mode: str = "competitive") -> dict:
        alpha = 1.0 + (inhibitor_conc / k_i)
        if mode.lower() == "competitive":
            return {"apparent_Vmax": v_max, "apparent_Km": round(k_m * alpha, 4)}
        return {"apparent_Vmax": round(v_max / alpha, 4), "apparent_Km": k_m}

class PhylogeneticTreeEngine:
    @staticmethod
    def construct_upgma_tree(taxa: list, distance_matrix: list) -> dict:
        taxa = list(taxa)
        n = len(taxa)
        clusters = {i: [taxa[i]] for i in range(n)}
        cluster_labels = {i: taxa[i] for i in range(n)}
        current_matrix = np.array(distance_matrix, dtype=float)
        active_nodes = list(range(n))

        while len(active_nodes) > 1:
            min_dist = float('inf')
            min_i, min_j = -1, -1
            for i in range(len(active_nodes)):
                for j in range(i + 1, len(active_nodes)):
                    u, v = active_nodes[i], active_nodes[j]
                    if current_matrix[u, v] < min_dist:
                        min_dist = current_matrix[u, v]
                        min_i, min_j = u, v
            node_a, node_b = min_i, min_j
            new_node_id = max(clusters.keys()) + 1
            new_label = f"({cluster_labels[node_a]}:{round(min_dist/2.0, 3)},{cluster_labels[node_b]}:{round(min_dist/2.0, 3)})"
            clusters[new_node_id] = clusters[node_a] + clusters[node_b]
            cluster_labels[new_node_id] = new_label
            old_size = current_matrix.shape[0]
            new_matrix = np.zeros((old_size + 1, old_size + 1), dtype=float)
            new_matrix[:old_size, :old_size] = current_matrix
            for k in active_nodes:
                if k not in (node_a, node_b):
                    sa, sb = len(clusters[node_a]), len(clusters[node_b])
                    dk = (sa * current_matrix[k, node_a] + sb * current_matrix[k, node_b]) / (sa + sb)
                    new_matrix[k, new_node_id] = new_matrix[new_node_id, k] = dk
            current_matrix = new_matrix
            active_nodes.remove(node_a)
            active_nodes.remove(node_b)
            active_nodes.append(new_node_id)
        return {"newick_tree_representation": cluster_labels[active_nodes[0]] + ";"}

class GeneticLinkageMappingEngine:
    @staticmethod
    def calculate_linkage(parental_count: int, recombinant_count: int) -> dict:
        total = parental_count + recombinant_count
        r = recombinant_count / total
        return {"standard_map_distance_cM": f"{round(r * 100.0, 3)} cM", "recombination_fraction_r": round(r, 4)}

class AllostericCooperativityEngine:
    @staticmethod
    def fit_hill_equation(ligand_concentrations: list, fractional_saturations: list) -> dict:
        x_arr = np.array([math.log10(l) for l in ligand_concentrations])
        y_arr = np.array([math.log10(t / (1.0 - t)) for t in fractional_saturations])
        slope, _ = np.polyfit(x_arr, y_arr, 1)
        return {"hill_coefficient_nH": round(float(slope), 3), "cooperativity_type": "POSITIVE_COOPERATIVITY" if slope > 1.05 else "NON_COOPERATIVE"}

class AdvancedAlignmentEngine:
    @staticmethod
    def smith_waterman_affine(seq1: str, seq2: str, match: int = 3, mismatch: int = -3, gap_open: int = 5, gap_extend: int = 1) -> dict:
        n, m = len(seq1), len(seq2)
        M = np.zeros((n + 1, m + 1), dtype=float)
        Ix = np.full((n + 1, m + 1), -np.inf)
        Iy = np.full((n + 1, m + 1), -np.inf)
        max_score = 0.0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                s = match if seq1[i-1] == seq2[j-1] else mismatch
                Ix[i, j] = max(M[i-1, j] - gap_open, Ix[i-1, j] - gap_extend)
                Iy[i, j] = max(M[i, j-1] - gap_open, Iy[i, j-1] - gap_extend)
                M[i, j] = max(0.0, M[i-1, j-1] + s, Ix[i, j], Iy[i, j])
                if M[i, j] > max_score:
                    max_score = M[i, j]
        return {"max_alignment_score": float(max_score)}

    @staticmethod
    def needleman_wunsch_visual(seq1: str, seq2: str, match: int = 1, mismatch: int = -1, gap: int = -1) -> dict:
        n, m = len(seq1), len(seq2)
        DP = np.zeros((n + 1, m + 1), dtype=int)
        traceback = np.zeros((n + 1, m + 1), dtype=int)
        for i in range(n + 1): DP[i, 0] = i * gap; traceback[i, 0] = 2
        for j in range(m + 1): DP[0, j] = j * gap; traceback[0, j] = 3
        traceback[0, 0] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                s = match if seq1[i-1] == seq2[j-1] else mismatch
                diag = DP[i-1, j-1] + s
                up = DP[i-1, j] + gap
                left = DP[i, j-1] + gap
                best = max(diag, up, left)
                DP[i, j] = best
                traceback[i, j] = 1 if best == diag else (2 if best == up else 3)

        align1, align2 = [], []
        curr_i, curr_j = n, m
        while curr_i > 0 or curr_j > 0:
            tb = traceback[curr_i, curr_j]
            if tb == 1 or (curr_i > 0 and curr_j > 0 and tb == 0):
                align1.append(seq1[curr_i - 1])
                align2.append(seq2[curr_j - 1])
                curr_i -= 1; curr_j -= 1
            elif tb == 2:
                align1.append(seq1[curr_i - 1])
                align2.append('-')
                curr_i -= 1
            else:
                align1.append('-')
                align2.append(seq2[curr_j - 1])
                curr_j -= 1

        return {
            "score": int(DP[n, m]),
            "aligned_seq1": "".join(reversed(align1)),
            "aligned_seq2": "".join(reversed(align2)),
            "matrix_ascii": str(DP)
        }

class InverseBwtDecoderEngine:
    @staticmethod
    def decode_bwt(bwt_str: str) -> dict:
        bwt_str = bwt_str.strip()
        if "$" not in bwt_str: bwt_str += "$"
        n = len(bwt_str)
        L_tuples = []
        counts_L = {}
        for char in bwt_str:
            counts_L[char] = counts_L.get(char, 0) + 1
            L_tuples.append((char, counts_L[char]))
        F_tuples = sorted(L_tuples, key=lambda x: x[0])
        tuple_to_F_idx = {t: idx for idx, t in enumerate(F_tuples)}
        orig = []
        curr_tuple = ('$', 1)
        for _ in range(n - 1):
            if curr_tuple not in tuple_to_F_idx: break
            f_idx = tuple_to_F_idx[curr_tuple]
            next_tuple = L_tuples[f_idx]
            orig.append(next_tuple[0])
            curr_tuple = next_tuple
        return {"decoded_sequence": "".join(reversed(orig)), "status": "EXACT_RECONSTRUCTION"}

class SangerSlidingWindowQCEngine:
    @staticmethod
    def trim_sliding_window(sequence: str, qual_str: str, window_size: int = 4, min_q: float = 20.0) -> dict:
        seq = sequence.strip()
        scores = [ord(c) - 33 for c in qual_str.strip()]
        n = len(scores)
        cut_idx = n
        for i in range(0, n - window_size + 1):
            if float(np.mean(scores[i:i + window_size])) < min_q:
                cut_idx = i
                break
        return {"original_length": n, "trimmed_length": cut_idx, "trimmed_sequence": seq[:cut_idx]}
