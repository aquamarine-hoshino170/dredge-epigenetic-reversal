import numpy as np
import math
import random
from concurrent.futures import ThreadPoolExecutor

class MultithreadedBWTEngine:
    r"""
    Multithreaded FM-Index Search Engine with Array Optimization
    """
    @staticmethod
    def _build_index(text: str):
        s = text.strip()
        if "$" not in s:
            s += "$"
        n = len(s)
        rotations = sorted([s[i:] + s[:i] for i in range(n)])
        bwt_str = "".join([r[-1] for r in rotations])
        alphabet = sorted(list(set(bwt_str)))
        
        counts = {char: bwt_str.count(char) for char in alphabet}
        C = {}
        total = 0
        for char in alphabet:
            C[char] = total
            total += counts[char]
            
        Occ = {char: np.zeros(n + 1, dtype=int) for char in alphabet}
        for i, char in enumerate(bwt_str):
            for c in alphabet:
                Occ[c][i + 1] = Occ[c][i] + (1 if char == c else 0)
                
        return bwt_str, C, Occ, n

    @staticmethod
    def _search_single(pattern: str, C: dict, Occ: dict, n: int) -> int:
        l, r = 0, n
        for char in reversed(pattern):
            if char not in C:
                return 0
            l = C[char] + Occ[char][l]
            r = C[char] + Occ[char][r]
            if l >= r:
                return 0
        return int(r - l)

    @staticmethod
    def parallel_bwt_search(text: str, patterns: list, workers: int = 4) -> dict:
        bwt_str, C, Occ, n = MultithreadedBWTEngine._build_index(text)
        results = {}
        with ThreadPoolExecutor(max_workers=workers) as executor:
            future_to_pat = {executor.submit(MultithreadedBWTEngine._search_single, pat, C, Occ, n): pat for pat in patterns}
            for future in future_to_pat:
                pat = future_to_pat[future]
                results[pat] = future.result()
        return {
            "bwt_length": n,
            "patterns_queried": len(patterns),
            "matches": results,
            "engine": "Multithreaded Parallel FM-Index"
        }

class Constrained3DRNAEngine:
    r"""
    3D Spatial Constraint-Aware Nussinov Folding Energy Minimizer
    """
    CANONICAL = {('A', 'U'), ('U', 'A'), ('G', 'C'), ('C', 'G'), ('G', 'U'), ('U', 'G')}

    @staticmethod
    def fold_3d_constrained(rna_seq: str, distance_matrix: list, opt_dist: float = 12.0, max_tol: float = 20.0) -> dict:
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
                    spatial_score = max(0.0, 1.0 - (abs(dist - opt_dist) / max_tol))
                    DP[i, j] = max(DP[i, j], DP[i + 1, j - 1] + 1.0 + spatial_score)
                for k in range(i + 1, j):
                    DP[i, j] = max(DP[i, j], DP[i, k] + DP[k + 1, j])

        return {
            "rna_length": n,
            "max_constrained_energy_score": round(float(DP[0, n - 1]), 4),
            "folding_model": "3D Distance-Constrained Nussinov Lattice"
        }

class GillespieStochasticKineticsEngine:
    r"""
    Continuous-Time Stochastic Markov Simulation via Gillespie Direct Method
    """
    @staticmethod
    def simulate_trajectory(s_init: int = 1000, e_init: int = 100, k1: float = 0.001, k2: float = 0.1, k3: float = 0.5, t_max: float = 5.0) -> dict:
        S, E, ES, P = s_init, e_init, 0, 0
        t = 0.0
        events = 0
        p_trajectory = []

        while t < t_max and (S > 0 or ES > 0):
            a1 = k1 * S * E
            a2 = k2 * ES
            a3 = k3 * ES
            a0 = a1 + a2 + a3
            if a0 <= 0:
                break

            r1 = max(1e-12, random.random())
            r2 = random.random()
            tau = -math.log(r1) / a0
            t += tau

            rand_a = r2 * a0
            if rand_a < a1:
                S -= 1; E -= 1; ES += 1
            elif rand_a < a1 + a2:
                S += 1; E += 1; ES -= 1
            else:
                ES -= 1; E += 1; P += 1

            events += 1
            if events % 100 == 0:
                p_trajectory.append((round(t, 4), P))

        p_trajectory.append((round(t, 4), P))
        return {
            "total_stochastic_events": events,
            "final_simulation_time": round(t, 4),
            "final_substrate": S,
            "final_product": P,
            "trajectory_samples": p_trajectory[-4:]
        }

class JukesCantorMLEngine:
    r"""
    Jukes-Cantor (JC69) Maximum Likelihood Branch Estimation via Grid Optimization
    """
    @staticmethod
    def calculate_ml_branch(seq1: str, seq2: str) -> dict:
        s1, s2 = seq1.upper().strip(), seq2.upper().strip()
        n = min(len(s1), len(s2))
        diffs = sum(1 for i in range(n) if s1[i] != s2[i])
        p_dist = diffs / n if n > 0 else 0.0

        if p_dist >= 0.75:
            return {"error": "Saturation limit reached (p-distance >= 0.75)"}

        best_t = 0.001
        max_log_l = -np.inf
        
        for t in np.linspace(0.001, 1.5, 1500):
            p_same = max(1e-15, 0.25 + 0.75 * math.exp(-4.0 * t / 3.0))
            p_diff = max(1e-15, 0.25 - 0.25 * math.exp(-4.0 * t / 3.0))
            log_l = ((n - diffs) * math.log(p_same)) + (diffs * math.log(p_diff))
            if log_l > max_log_l:
                max_log_l = log_l
                best_t = t

        return {
            "aligned_sites": n,
            "observed_mutations": diffs,
            "p_distance": round(p_dist, 4),
            "max_likelihood_branch_t": round(float(best_t), 4),
            "log_likelihood": round(float(max_log_l), 4)
        }

class DeBruijnGraphCorrectionEngine:
    r"""
    Next-Gen Sequencing Error Correction via de Bruijn Directional k-mer Networks
    """
    @staticmethod
    def repair_reads(reads: list, k: int = 3, min_cov: int = 2) -> dict:
        kmer_counts = {}
        for r in reads:
            for i in range(len(r) - k + 1):
                kmer = r[i:i+k]
                kmer_counts[kmer] = kmer_counts.get(kmer, 0) + 1

        solid_kmers = {kmer for kmer, c in kmer_counts.items() if c >= min_cov}
        repaired = []
        corrections_count = 0

        for r in reads:
            r_chars = list(r)
            for i in range(len(r) - k + 1):
                kmer = "".join(r_chars[i:i+k])
                if kmer not in solid_kmers:
                    for base in ['A', 'C', 'G', 'T']:
                        for pos in range(k):
                            mut = list(kmer)
                            mut[pos] = base
                            candidate = "".join(mut)
                            if candidate in solid_kmers:
                                r_chars[i + pos] = base
                                corrections_count += 1
                                break
            repaired.append("".join(r_chars))

        return {
            "total_kmers": len(kmer_counts),
            "solid_kmers": len(solid_kmers),
            "corrections_applied": corrections_count,
            "repaired_sequences": repaired
        }
