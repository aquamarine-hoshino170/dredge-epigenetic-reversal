import numpy as np
import math

class GrandFinaleBioEngine:
    r"""
    1. Smith-Waterman with 3-State Affine Matrices (M, Ix, Iy) & Backtracking Vectors
    2. Needleman-Wunsch with Extended Affine Scoring
    """
    @staticmethod
    def smith_waterman_full_affine(seq1: str, seq2: str, match: int = 3, mismatch: int = -3, gap_open: int = 5, gap_extend: int = 1) -> dict:
        n, m = len(seq1), len(seq2)
        M = np.zeros((n + 1, m + 1), dtype=float)
        Ix = np.full((n + 1, m + 1), -np.inf)
        Iy = np.full((n + 1, m + 1), -np.inf)
        trace = np.zeros((n + 1, m + 1), dtype=int) # 0: Stop, 1: Diag(M), 2: Up(Ix), 3: Left(Iy)

        max_score = 0.0
        max_pos = (0, 0)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                s = match if seq1[i-1] == seq2[j-1] else mismatch
                Ix[i, j] = max(M[i-1, j] - gap_open, Ix[i-1, j] - gap_extend)
                Iy[i, j] = max(M[i, j-1] - gap_open, Iy[i, j-1] - gap_extend)
                
                diag = M[i-1, j-1] + s
                best = max(0.0, diag, Ix[i, j], Iy[i, j])
                M[i, j] = best

                if best == 0.0:
                    trace[i, j] = 0
                elif best == diag:
                    trace[i, j] = 1
                elif best == Ix[i, j]:
                    trace[i, j] = 2
                else:
                    trace[i, j] = 3

                if best > max_score:
                    max_score = best
                    max_pos = (i, j)

        # Backtrack optimal local strand
        ci, cj = max_pos
        a1, a2 = [], []
        while ci > 0 and cj > 0 and M[ci, cj] > 0:
            tr = trace[ci, cj]
            if tr == 1:
                a1.append(seq1[ci-1])
                a2.append(seq2[cj-1])
                ci -= 1; cj -= 1
            elif tr == 2:
                a1.append(seq1[ci-1])
                a2.append('-')
                ci -= 1
            elif tr == 3:
                a1.append('-')
                a2.append(seq2[cj-1])
                cj -= 1
            else:
                break

        return {
            "max_score": float(max_score),
            "peak_coordinate": max_pos,
            "local_align_seq1": "".join(reversed(a1)),
            "local_align_seq2": "".join(reversed(a2)),
            "matrix_M": str(M),
            "matrix_Ix": str(Ix),
            "matrix_Iy": str(Iy)
        }

    @staticmethod
    def needleman_wunsch_affine(seq1: str, seq2: str, match: int = 2, mismatch: int = -2, gap_open: int = 4, gap_extend: int = 1) -> dict:
        n, m = len(seq1), len(seq2)
        M = np.zeros((n + 1, m + 1), dtype=float)
        Ix = np.full((n + 1, m + 1), -np.inf)
        Iy = np.full((n + 1, m + 1), -np.inf)

        for i in range(1, n + 1):
            M[i, 0] = -gap_open - (i - 1) * gap_extend
            Ix[i, 0] = M[i, 0]
        for j in range(1, m + 1):
            M[0, j] = -gap_open - (j - 1) * gap_extend
            Iy[0, j] = M[0, j]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                s = match if seq1[i-1] == seq2[j-1] else mismatch
                Ix[i, j] = max(M[i-1, j] - gap_open, Ix[i-1, j] - gap_extend)
                Iy[i, j] = max(M[i, j-1] - gap_open, Iy[i, j-1] - gap_extend)
                M[i, j] = max(M[i-1, j-1] + s, Ix[i, j], Iy[i, j])

        return {
            "global_affine_score": float(M[n, m]),
            "matrix_shape": f"{n}x{m}"
        }

class FMIndexBwtEngine:
    r"""
    BWT Matrix & Full FM-Index String Matching (Count & Locate)
    """
    @staticmethod
    def build_fm_index(text: str) -> dict:
        s = text.strip()
        if "$" not in s: s += "$"
        n = len(s)
        rotations = sorted([s[i:] + s[:i] for i in range(n)])
        bwt_str = "".join([r[-1] for r in rotations])
        
        # Build C-table (Count of characters lexicographically smaller)
        alphabet = sorted(list(set(bwt_str)))
        counts = {char: bwt_str.count(char) for char in alphabet}
        C = {}
        total = 0
        for char in alphabet:
            C[char] = total
            total += counts[char]

        # Build Occ-table (Occurrence matrix)
        Occ = {char: [0] * (n + 1) for char in alphabet}
        for i, char in enumerate(bwt_str):
            for c in alphabet:
                Occ[c][i + 1] = Occ[c][i] + (1 if char == c else 0)

        return {
            "bwt_transformed": bwt_str,
            "alphabet": alphabet,
            "C_table": C,
            "rotations_preview": rotations[:5],
            "_internal": (bwt_str, C, Occ, n)
        }

    @staticmethod
    def count_pattern(pattern: str, text: str) -> dict:
        fm = FMIndexBwtEngine.build_fm_index(text)
        bwt_str, C, Occ, n = fm["_internal"]
        
        l, r = 0, n
        for char in reversed(pattern):
            if char not in C:
                return {"pattern": pattern, "occurrences": 0, "status": "NOT_FOUND"}
            l = C[char] + Occ[char][l]
            r = C[char] + Occ[char][r]
            if l >= r:
                return {"pattern": pattern, "occurrences": 0, "status": "NOT_FOUND"}

        return {
            "pattern": pattern,
            "occurrences": r - l,
            "range": [l, r],
            "bwt_source": bwt_str,
            "status": "EXACT_MATCH"
        }

class AdaptivePhredTrimmerEngine:
    r"""
    Adaptive Sliding Window FastQ Trimmer with Variance & Std-Dev
    """
    @staticmethod
    def adaptive_trim(sequence: str, qual_str: str, min_q: float = 20.0, base_window: int = 4) -> dict:
        seq = sequence.strip()
        scores = [ord(c) - 33 for c in qual_str.strip()]
        n = len(scores)
        
        if n == 0:
            return {"error": "Empty sequence"}

        cut_idx = n
        i = 0
        while i < n:
            # Dynamic window expansion based on localized variance
            local_slice = scores[i:min(n, i + base_window)]
            var = float(np.var(local_slice)) if len(local_slice) > 1 else 0.0
            win_size = max(2, int(base_window - 1)) if var > 50.0 else base_window

            curr_win = scores[i:min(n, i + win_size)]
            mean_q = float(np.mean(curr_win))

            if mean_q < min_q:
                cut_idx = i
                break
            i += 1

        trimmed_seq = seq[:cut_idx]
        dropped = n - cut_idx
        return {
            "original_length": n,
            "trimmed_length": cut_idx,
            "trimmed_sequence": trimmed_seq,
            "data_drop_pct": f"{round((dropped / n) * 100.0, 2)}%",
            "overall_phred_mean": round(float(np.mean(scores)), 2),
            "overall_phred_std": round(float(np.std(scores)), 2)
        }

class NonLinearKineticsEngine:
    r"""
    Direct Non-Linear Least Squares Fit for Michaelis-Menten Kinetics
    v = (Vmax * [S]) / (Km + [S])  [Gauss-Newton Numerical Optimizer]
    """
    @staticmethod
    def fit_direct_nls(substrates: list, velocities: list, max_iter: int = 100, tol: float = 1e-6) -> dict:
        s = np.array(substrates, dtype=float)
        v = np.array(velocities, dtype=float)

        # Initial estimation via median and max
        v_max = float(np.max(v)) * 1.1
        k_m = float(np.median(s))

        for _ in range(max_iter):
            pred_v = (v_max * s) / (k_m + s)
            residuals = v - pred_v

            # Jacobian matrix: [dv/dVmax, dv/dKm]
            J = np.zeros((len(s), 2))
            J[:, 0] = s / (k_m + s)                       # dv/dVmax
            J[:, 1] = -(v_max * s) / ((k_m + s) ** 2)     # dv/dKm

            # Normal equations: (J^T * J) * delta = J^T * residuals
            try:
                delta = np.linalg.lstsq(J, residuals, rcond=None)[0]
            except Exception:
                break

            v_max += delta[0]
            k_m += delta[1]

            if np.linalg.norm(delta) < tol or v_max <= 0 or k_m <= 0:
                break

        # Calculate final R-squared
        final_pred = (v_max * s) / (k_m + s)
        ss_res = np.sum((v - final_pred) ** 2)
        ss_tot = np.sum((v - np.mean(v)) ** 2)
        r2 = 1.0 - (ss_res / ss_tot) if ss_tot > 0 else 1.0

        return {
            "v_max": round(float(v_max), 4),
            "k_m": round(float(k_m), 4),
            "r_squared": round(float(r2), 4),
            "fitting_algorithm": "Non-Linear Gauss-Newton Least Squares"
        }

class ExactTreeBranchEngine:
    r"""
    Multi-Taxa UPGMA Parser with Exact Branch Length Fractions
    """
    @staticmethod
    def construct_verified_upgma(taxa: list, distance_matrix: list) -> dict:
        taxa = list(taxa)
        n = len(taxa)
        clusters = {i: [taxa[i]] for i in range(n)}
        cluster_labels = {i: taxa[i] for i in range(n)}
        node_heights = {i: 0.0 for i in range(n)}
        current_matrix = np.array(distance_matrix, dtype=float)
        active_nodes = list(range(n))
        branch_reports = []

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
            new_height = min_dist / 2.0
            
            branch_len_a = round(new_height - node_heights[node_a], 4)
            branch_len_b = round(new_height - node_heights[node_b], 4)
            
            new_label = f"({cluster_labels[node_a]}:{branch_len_a},{cluster_labels[node_b]}:{branch_len_b})"
            clusters[new_node_id] = clusters[node_a] + clusters[node_b]
            cluster_labels[new_node_id] = new_label
            node_heights[new_node_id] = new_height

            branch_reports.append({
                "merged": f"{cluster_labels[node_a]} & {cluster_labels[node_b]}",
                "divergence_height": round(new_height, 4),
                "branch_fraction_a": branch_len_a,
                "branch_fraction_b": branch_len_b
            })

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

        return {
            "newick_tree": cluster_labels[active_nodes[0]] + ";",
            "branch_reports": branch_reports,
            "root_tree_height": round(node_heights[active_nodes[0]], 4)
        }

# Previous verified base classes
class PureThermodynamicsEngine:
    NN_DATA = {
        'AA': (-7.6, -21.3), 'TT': (-7.6, -21.3), 'AT': (-7.2, -20.4), 'TA': (-7.2, -21.3),
        'CA': (-8.5, -22.7), 'TG': (-8.5, -22.7), 'GT': (-8.4, -22.4), 'AC': (-8.4, -22.4),
        'CT': (-7.8, -21.0), 'AG': (-7.8, -21.0), 'GA': (-8.2, -22.2), 'TC': (-8.2, -22.2),
        'CG': (-10.6, -27.2), 'GC': (-9.8, -24.4), 'GG': (-8.0, -19.9), 'CC': (-8.0, -19.9)
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
        tm_k = (dh * 1000.0) / (ds + 1.9872 * math.log((primer_conc_nM * 1e-9) / 4.0))
        return {
            "melting_temperature_Tm": f"{round(tm_k - 273.15, 2)} °C",
            "gibbs_free_energy_dG_37C": f"{round(dh - (310.15 * ds / 1000.0), 2)} kcal/mol"
        }

class PureBiochemistryProteinEngine:
    PKA_VALUES = {'N_term': 9.69, 'C_term': 2.34, 'C': 8.33, 'D': 3.86, 'E': 4.25, 'H': 6.00, 'K': 10.53, 'R': 12.48, 'Y': 10.07}
    @staticmethod
    def _charge(seq: str, ph: float) -> float:
        ch = 1.0 / (1.0 + 10.0 ** (ph - PureBiochemistryProteinEngine.PKA_VALUES['N_term']))
        for r in ['K', 'R', 'H']: ch += seq.count(r) * (1.0 / (1.0 + 10.0 ** (ph - PureBiochemistryProteinEngine.PKA_VALUES[r])))
        ch -= 1.0 / (1.0 + 10.0 ** (PureBiochemistryProteinEngine.PKA_VALUES['C_term'] - ph))
        for r in ['D', 'E', 'C', 'Y']: ch -= seq.count(r) * (1.0 / (1.0 + 10.0 ** (PureBiochemistryProteinEngine.PKA_VALUES[r] - ph)))
        return ch
    @staticmethod
    def calculate_isoelectric_point(protein_seq: str) -> dict:
        seq = protein_seq.upper().strip()
        low, high = 0.0, 14.0
        for _ in range(50):
            mid = (low + high) / 2.0
            if PureBiochemistryProteinEngine._charge(seq, mid) > 0: low = mid
            else: high = mid
        return {"isoelectric_point_pI": round((low + high) / 2.0, 3)}

class PureMolecularGenomicsEngine:
    CODON_MAP = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*', 'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'}
    @staticmethod
    def translate(dna_seq: str) -> str:
        s = dna_seq.upper().replace(' ', '')
        return "".join([PureMolecularGenomicsEngine.CODON_MAP.get(s[i:i+3], '?') for i in range(0, len(s) - 2, 3)])
