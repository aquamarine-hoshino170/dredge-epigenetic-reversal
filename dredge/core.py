import numpy as np

class HorvathEpigeneticClock:
    """
    Simulates elastic-net penalized epigenetic biological age estimation.
    """
    def __init__(self, n_sites: int = 1000):
        np.random.seed(42)
        self.weights = np.random.normal(loc=0.05, scale=0.02, size=n_sites)
        self.intercept = 20.0

    def predict_age(self, methylation_states: np.ndarray) -> float:
        """Predicts biological age from CpG methylation vector."""
        raw_age = self.intercept + np.dot(methylation_states, self.weights)
        return float(np.clip(raw_age, 0.0, 120.0))


class WaddingtonPotentialEngine:
    """
    Ultra-tier Epigenetic Entropy Reversal Engine with Horvath Clock Calibration.
    """
    def __init__(self, n_cpg_sites: int = 2000, temperature: float = 0.04):
        self.n_sites = n_cpg_sites
        self.temp = temperature
        self.clock = HorvathEpigeneticClock(n_sites=n_cpg_sites)
        # Old/degraded epigenetic state
        self.state = np.random.beta(a=0.8, b=0.3, size=self.n_sites)

    def calculate_shannon_entropy(self, p: np.ndarray) -> float:
        eps = 1e-12
        p_c = np.clip(p, eps, 1.0 - eps)
        s_i = -(p_c * np.log2(p_c) + (1.0 - p_c) * np.log2(1.0 - p_c))
        return float(np.mean(s_i))

    def potential_gradient(self, p: np.ndarray) -> np.ndarray:
        return 4.0 * (p - 0.5)**3 - 2.0 * (p - 0.5)

    def simulate_tet2_reversal(self, steps: int = 150, catalytic_rate: float = 0.35, dt: float = 0.01) -> dict:
        initial_entropy = self.calculate_shannon_entropy(self.state)
        initial_age = self.clock.predict_age(self.state)
        
        entropy_traj = [initial_entropy]
        age_traj = [initial_age]
        
        current_p = self.state.copy()
        
        for _ in range(steps):
            drift = -self.potential_gradient(current_p)
            tet2_force = -catalytic_rate * current_p
            diffusion = np.sqrt(2.0 * self.temp * dt) * np.random.normal(size=self.n_sites)
            
            current_p = np.clip(current_p + (drift + tet2_force) * dt + diffusion, 0.0, 1.0)
            entropy_traj.append(self.calculate_shannon_entropy(current_p))
            age_traj.append(self.clock.predict_age(current_p))
            
        self.state = current_p
        
        return {
            "initial_entropy": initial_entropy,
            "final_entropy": entropy_traj[-1],
            "initial_age": initial_age,
            "final_age": age_traj[-1],
            "age_reversal_years": initial_age - age_traj[-1],
            "entropy_reduction_pct": ((entropy_traj[-1] - initial_entropy) / initial_entropy) * 100.0,
            "entropy_traj": entropy_traj,
            "age_traj": age_traj
        }
