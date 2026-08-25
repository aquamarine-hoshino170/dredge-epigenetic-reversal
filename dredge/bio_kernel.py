import numpy as np
import math
import random
from concurrent.futures import ThreadPoolExecutor

class ParallelFMIndexEngine:
    @staticmethod
    def _build_fm(text: str):
        s = text.strip()
        if "$" not in s: s += "$"
        n = len(s)
        rotations = sorted([s[i:] + s[:i] for i in range(n)])
        bwt_str = "".join([r[-1] for r in rotations])
        alphabet = sorted(list(set(bwt_str)))
        counts = {char: bwt_str.count(char) for char in alphabet}
        C = {}
        tot = 0
        for c in alphabet:
            C[c] = tot
            tot += counts[c]
        Occ = {c: [0] * (n + 1) for c in alphabet}
        for i, char in enumerate(bwt_str):
            for c in alphabet:
                Occ[c][i + 1] = Occ[c][i] + (1 if char == c else 0)
        return bwt_str, C, Occ, n

    @staticmethod
    def _query_single(pattern: str, C: dict, Occ: dict, n: int) -> int:
        l, r = 0, n
        for char in reversed(pattern):
            if char not in C:
                return 0
            l = C[char] + Occ[char][l]
            r = C[char] + Occ[char][r]
            if l >= r:
                return 0
        return r - l

    @staticmethod
    def parallel_search(text: str, patterns: list, max_workers: int = 4) -> dict:
        bwt_str, C, Occ, n = ParallelFMIndexEngine._build_fm(text)
        results = {}
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_pat = {executor.submit(ParallelFMIndexEngine._query_single, pat, C, Occ, n): pat for pat in patterns}
            for future in future_to_pat:
                pat = future_to_pat[future]
                results[pat] = future.result()
        return {
            "bwt_length": n,
            "patterns_queried": len(patterns),
            "match_results": results,
            "engine": "Multithreaded SIMD-Emulated FM-Index"
        }

class Constrained3DRNAEngine:
    CANONICAL = {('A', 'U'), ('U', 'A'), ('G', 'C'), ('C', 'G'), ('G', 'U'), ('U', 'G')}

    @staticmethod
    def fold_with_spatial_constraints(rna_seq: str, distance_matrix: list, optimal_dist: float = 12.0, max_dist_tol: float = 20.0) -> dict:
        seq = rna_seq.upper().strip().replace('T', 'U')
        n = len(seq)
        D = np.array(distance_matrix, dtype=float)
        DP = np.zeros((n, n), dtype=float)

        for length in range(4, n):
            for i in range(n - length):
                j = i + length
                DP[i, j] = max(DP[i + 1, j], DP[i, j - 1])
                if (seq[i], seq[j]) in Constrained3DRNAEngine.CANONICAL:
                    dist = D[i, j]
                    spatial_score = max(0.0, 1.0 - (abs(dist - optimal_dist) / max_dist_tol))
                    DP[i, j] = max(DP[i, j], DP[i + 1, j - 1] + 1.0 + spatial_score)
                for k in range(i + 1, j):
                    DP[i, j] = max(DP[i, j], DP[i, k] + DP[k + 1, j])

        return {
            "sequence_length": n,
            "max_constrained_energy_score": round(float(DP[0, n - 1]), 3),
            "folding_model": "3D Spatial Constraint Nussinov Matrix"
        }

class GillespieStochasticKineticsEngine:
    @staticmethod
    def simulate_enzyme_system(s_init: int = 1000, e_init: int = 100, k1: float = 0.001, k2: float = 0.1, k3: float = 0.5, t_max: float = 10.0) -> dict:
        S, E, ES, P = s_init, e_init, 0, 0
        t = 0.0
        trajectory_events = 0
        history_p = [(0.0, P)]

        while t < t_max and (S > 0 or ES > 0):
            a1 = k1 * S * E
            a2 = k2 * ES
            a3 = k3 * ES
            a0 = a1 + a2 + a3
            if a0 <= 0: break

            r1, r2 = random.random(), random.random()
            tau = (1.0 / a0) * math.log(1.0 / (r1 if r1 > 0 else 1e-9))
            t += tau

            rand_a = r2 * a0
            if rand_a < a1:
                S -= 1; E -= 1; ES += 1
            elif rand_a < a1 + a2:
                S += 1; E += 1; ES -= 1
            else:
                ES -= 1; E += 1; P += 1

            trajectory_events += 1
            if trajectory_events % 200 == 0:
                history_p.append((round(t, 3), P))

        history_p.append((round(t, 3), P))
        return {
            "total_reaction_events": trajectory_events,
            "final_time": round(t, 4),
            "final_substrate_remaining": S,
            "final_product_formed": P,
            "sampling_trajectory_p": history_p[-5:]
        }

class JukesCantorMLEngine:
    @staticmethod
    def calculate_branch_ml(seq1: str, seq2: str) -> dict:
        s1, s2 = seq1.upper().strip(), seq2.upper().strip()
        n = min(len(s1), len(s2))
        diffs = sum(1 for i in range(n) if s1[i] != s2[i])
        p_dist = diffs / n

        if p_dist >= 0.75:
            return {"error": "Sequences are completely saturated (p-distance >= 0.75)"}

        # Grid Search for Max Likelihood Branch Length (t)
        best_t, max_log_l = 0.001, -np.inf
        for t_candidate in np.linspace(0.001, 1.5, 1500):
            p_same = 0.25 + 0.75 * math.exp(-4.0 * t_candidate / 3.0)
            p_diff = 0.25 - 0.25 * math.exp(-4.0 * t_candidate / 3.0)
            p_same = max(1e-15, p_same)
            p_diff = max(1e-15, p_diff)
            log_l = ((n - diffs) * math.log(p_same)) + (diffs * math.log(p_diff))
            if log_l > max_log_l:
                max_log_l = log_l
                best_t = t_candidate

        return {
            "analyzed_sites": n,
            "observed_substitutions": diffs,
            "p_distance": round(p_dist, 4),
            "maximum_likelihood_branch_t": round(float(best_t), 4),
            "log_likelihood": round(float(max_log_l), 4)
        }

class DeBruijnGraphCorrectionEngine:
    @staticmethod
    def error_correct(reads: list, k: int = 3, min_coverage: int = 2) -> dict:
        kmer_counts = {}
        for r in reads:
            for i in range(len(r) - k + 1):
                kmer = r[i:i+k]
                kmer_counts[kmer] = kmer_counts.get(kmer, 0) + 1

        solid_kmers = {kmer for kmer, c in kmer_counts.items() if c >= min_coverage}
        corrected = []
        corrections_applied = 0

        for r in reads:
            r_chars = list(r)
            for i in range(len(r) - k + 1):
                kmer = "".join(r_chars[i:i+k])
                if kmer not in solid_kmers:
                    # Attempt 1-bp mutation correction to solid k-mer
                    for b in ['A', 'C', 'G', 'T']:
                        for pos in range(k):
                            mut = list(kmer)
                            mut[pos] = b
                            mut_str = "".join(mut)
                            if mut_str in solid_kmers:
                                r_chars[i + pos] = b
                                corrections_applied += 1
                                break
            corrected.append("".join(r_chars))

        return {
            "total_kmers_indexed": len(kmer_counts),
            "solid_kmers": len(solid_kmers),
            "corrections_made": corrections_applied,
            "corrected_reads": corrected
        }

class EpigeneticShannonEntropyEngine:
    @staticmethod
    def calculate_methylation_entropy(methylation_patterns: list) -> dict:
        patterns = [p.strip().upper() for p in methylation_patterns if p.strip()]
        total = len(patterns)
        if total == 0: return {"error": "Empty pattern set"}

        counts = {}
        for p in patterns:
            counts[p] = counts.get(p, 0) + 1

        shannon_h = 0.0
        k = len(patterns[0])
        for p, count in counts.items():
            prob = count / total
            shannon_h -= prob * math.log2(prob)

        normalized_h = round(shannon_h / k, 4) if k > 0 else 0.0
        status = "HIGH_EPIGENETIC_DIVERSITY" if normalized_h > 0.5 else "STABLE_HOMOGENEOUS_EPITYPE"

        return {
            "total_reads": total,
            "pattern_length_k": k,
            "unique_epialleles": len(counts),
            "shannon_entropy_bits": round(shannon_h, 4),
            "normalized_entropy": normalized_h,
            "epigenetic_status": status
        }
