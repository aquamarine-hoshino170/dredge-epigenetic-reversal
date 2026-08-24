import numpy as np

class WaddingtonPotentialEngine:
    """
    Simulates Non-equilibrium Epigenetic Landscapes using Stochastic Langevin Dynamics.
    Aligned with MIT/Broad Institute Computational Epigenomics frameworks.
    """
    def __init__(self, n_cpg_sites: int = 1000, temperature: float = 0.05):
        self.n_sites = n_cpg_sites
        self.temp = temperature
        # Initialize degraded/aged epigenetic methylation state (High Entropy)
        self.state = np.random.beta(a=0.5, b=0.5, size=self.n_sites)

    def calculate_shannon_entropy(self, p: np.ndarray) -> float:
        """Computes information-theoretic Shannon entropy across CpG coordinates."""
        eps = 1e-12
        p_clamped = np.clip(p, eps, 1.0 - eps)
        s_i = -(p_clamped * np.log2(p_clamped) + (1.0 - p_clamped) * np.log2(1.0 - p_clamped))
        return float(np.mean(s_i))

    def potential_gradient(self, p: np.ndarray) -> np.ndarray:
        """
        Bistable epigenetic potential landscape V(p) = -a*(p - 0.5)^2 + b*(p - 0.5)^4
        Differentiating gives the drift term driving states to stable wells (0 or 1).
        """
        return 4.0 * (p - 0.5)**3 - 2.0 * (p - 0.5)

    def simulate_tet2_reversal(self, steps: int = 100, catalytic_rate: float = 0.15, dt: float = 0.01) -> dict:
        """
        Executes Euler-Maruyama integration over targeted TET2 demethylation vector fields.
        """
        initial_entropy = self.calculate_shannon_entropy(self.state)
        entropy_trajectory = [initial_entropy]
        
        current_p = self.state.copy()
        
        for step in range(steps):
            # Deterministic Waddington gradient drift
            drift = -self.potential_gradient(current_p)
            
            # Targeted TET2 catalytic active demethylation force
            tet2_force = -catalytic_rate * current_p
            
            # Stochastic thermal fluctuation (Brownian motion)
            diffusion = np.sqrt(2.0 * self.temp * dt) * np.random.normal(size=self.n_sites)
            
            # Update state with boundary clamping
            current_p = np.clip(current_p + (drift + tet2_force) * dt + diffusion, 0.0, 1.0)
            entropy_trajectory.append(self.calculate_shannon_entropy(current_p))
            
        self.state = current_p
        final_entropy = entropy_trajectory[-1]
        
        return {
            "initial_entropy_bits": initial_entropy,
            "final_entropy_bits": final_entropy,
            "entropy_delta_pct": ((final_entropy - initial_entropy) / initial_entropy) * 100.0,
            "methylation_mean": float(np.mean(current_p)),
            "methylation_variance": float(np.var(current_p)),
            "trajectory": entropy_trajectory
        }
