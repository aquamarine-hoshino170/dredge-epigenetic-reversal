import numpy as np
import math
import random

class HodgkinHuxleyCompartmentalEngine:
    r"""
    Multi-Compartmental Hodgkin-Huxley Cable Model (Non-Linear Ion Channel Dynamics)
    """
    @staticmethod
    def simulate_axon_cable(compartments: int = 10, total_time_ms: float = 5.0, dt: float = 0.025, inj_current: float = 15.0) -> dict:
        steps = int(total_time_ms / dt)
        V = np.full(compartments, -65.0) # Resting potential mV
        m = np.full(compartments, 0.05)
        h = np.full(compartments, 0.6)
        n = np.full(compartments, 0.32)

        C_m = 1.0       # uF/cm^2
        g_Na = 120.0    # mS/cm^2
        g_K = 36.0      # mS/cm^2
        g_L = 0.3       # mS/cm^2
        E_Na = 50.0     # mV
        E_K = -77.0     # mV
        E_L = -54.387   # mV
        ra = 10.0       # Axial resistance coupling (mS)

        voltage_grid = []

        for step in range(steps):
            # Injection current at compartment 0
            I_inj = inj_current if step * dt < 1.0 else 0.0

            # Compute axial diffusion (Laplacian cable operator)
            I_axial = np.zeros(compartments)
            for i in range(compartments):
                left = V[i-1] if i > 0 else V[i]
                right = V[i+1] if i < compartments - 1 else V[i]
                I_axial[i] = ra * (left - 2 * V[i] + right)

            for i in range(compartments):
                v = V[i]
                # Alpha & Beta functions
                alpha_m = 0.1 * (v + 40.0) / (1.0 - math.exp(-(v + 40.0) / 10.0)) if abs(v + 40.0) > 1e-6 else 1.0
                beta_m = 4.0 * math.exp(-(v + 65.0) / 18.0)
                alpha_h = 0.07 * math.exp(-(v + 65.0) / 20.0)
                beta_h = 1.0 / (1.0 + math.exp(-(v + 35.0) / 10.0))
                alpha_n = 0.01 * (v + 55.0) / (1.0 - math.exp(-(v + 55.0) / 10.0)) if abs(v + 55.0) > 1e-6 else 0.1
                beta_n = 0.125 * math.exp(-(v + 65.0) / 80.0)

                m[i] += dt * (alpha_m * (1.0 - m[i]) - beta_m * m[i])
                h[i] += dt * (alpha_h * (1.0 - h[i]) - beta_h * h[i])
                n[i] += dt * (alpha_n * (1.0 - n[i]) - beta_n * n[i])

                I_ion = g_Na * (m[i]**3) * h[i] * (v - E_Na) + g_K * (n[i]**4) * (v - E_K) + g_L * (v - E_L)
                inj = I_inj if i == 0 else 0.0
                V[i] += (dt / C_m) * (inj - I_ion + I_axial[i])

            if step % int(1.0 / dt) == 0:
                voltage_grid.append([round(float(val), 2) for val in V])

        return {
            "compartments_count": compartments,
            "simulation_steps": steps,
            "final_soma_voltage": round(float(V[0]), 2),
            "final_terminal_voltage": round(float(V[-1]), 2),
            "sampled_voltage_propagation": voltage_grid[-4:]
        }

class QuantumFMOExcitonEngine:
    r"""
    FMO Complex 7-Site Quantum Coherent Hamiltonian & Lindblad Dephasing Master Equation
    """
    @staticmethod
    def simulate_coherence_dynamics(steps: int = 50, dt_fs: float = 2.0, dephasing_rate: float = 0.005) -> dict:
        # Standard FMO 3-Site Sub-Hamiltonian (cm^-1 converted to normalized energy)
        H = np.array([
            [12410.0, -87.7, 5.5],
            [-87.7, 12530.0, 31.0],
            [5.5, 31.0, 12210.0]
        ], dtype=complex) / 1000.0

        # Initial density matrix: pure state on Site 1
        rho = np.zeros((3, 3), dtype=complex)
        rho[0, 0] = 1.0

        coherence_trace = []

        for _ in range(steps):
            # Commutator -i [H, rho]
            d_rho = -1j * (H @ rho - rho @ H)

            # Lindblad pure dephasing off-diagonals
            for i in range(3):
                for j in range(3):
                    if i != j:
                        d_rho[i, j] -= dephasing_rate * rho[i, j]

            rho += d_rho * (dt_fs / 10.0)
            # Maintain trace normalization
            rho /= np.trace(rho)
            coherence_trace.append(round(float(abs(rho[0, 1])), 5))

        return {
            "quantum_system": "FMO Light-Harvesting 3-Site Subcomplex",
            "initial_coherence": 1.0,
            "final_off_diagonal_coherence": coherence_trace[-1],
            "site_1_population": round(float(rho[0, 0].real), 4),
            "site_2_population": round(float(rho[1, 1].real), 4),
            "site_3_population": round(float(rho[2, 2].real), 4),
            "coherence_loss_trajectory": coherence_trace[::10]
        }

class TuringMorphogenesisEngine:
    r"""
    Turing Reaction-Diffusion 2D Activator-Inhibitor Pattern Formation
    """
    @staticmethod
    def render_turing_tissue(grid_size: int = 24, iterations: int = 150) -> dict:
        np.random.seed(42)
        u = np.ones((grid_size, grid_size)) + 0.05 * np.random.randn(grid_size, grid_size)
        v = np.zeros((grid_size, grid_size)) + 0.05 * np.random.randn(grid_size, grid_size)

        Du, Dv = 0.16, 0.08
        F, k = 0.035, 0.065
        dt = 1.0

        for _ in range(iterations):
            # 2D discrete 5-point stencil Laplacian with periodic boundary conditions
            lap_u = (np.roll(u, 1, axis=0) + np.roll(u, -1, axis=0) + np.roll(u, 1, axis=1) + np.roll(u, -1, axis=1) - 4 * u)
            lap_v = (np.roll(v, 1, axis=0) + np.roll(v, -1, axis=0) + np.roll(v, 1, axis=1) + np.roll(v, -1, axis=1) - 4 * v)

            uvv = u * v * v
            u += dt * (Du * lap_u - uvv + F * (1.0 - u))
            v += dt * (Dv * lap_v + uvv - (F + k) * v)

        # ASCII Render Matrix
        chars = [" ", "·", "x", "#"]
        ascii_grid = []
        for row in u:
            line = "".join([chars[min(3, max(0, int(val * 3.0)))] for val in row])
            ascii_grid.append(line)

        return {
            "grid_dimensions": f"{grid_size}x{grid_size}",
            "mean_activator_density": round(float(np.mean(u)), 4),
            "pattern_type": "Turing Self-Organizing Spots / Labyrinths",
            "ascii_visual": ascii_grid[:12]
        }

class DNAOrigamiScaffoldEngine:
    r"""
    3D DNA Origami Staple Routing & Mechanical Torsion Strain Tensor
    """
    @staticmethod
    def calculate_origami_torsion(scaffold_length: int, staple_count: int, cross_over_density: float = 1.5) -> dict:
        if scaffold_length < 100 or staple_count <= 0:
            return {"error": "Scaffold must be at least 100bp and staples > 0"}

        bp_per_turn = 10.5 # B-DNA helical pitch
        total_turns = scaffold_length / bp_per_turn
        ideal_crossovers = int(total_turns * cross_over_density)

        # Angular mismatch torsion strain (Frank-Kamenetskii energy model)
        twist_per_bp = 34.28 # degrees
        accumulated_twist = (scaffold_length * twist_per_bp) % 360.0
        torsional_strain_energy = round(0.5 * 0.04 * (accumulated_twist ** 2), 2) # pN * nm

        stability_verdict = "RIGID_NANOROBOT_STRUCTURE" if torsional_strain_energy < 500.0 else "HIGH_INTERNAL_SHEAR_STRAIN"

        return {
            "scaffold_bases": scaffold_length,
            "total_staples_routed": staple_count,
            "optimal_crossover_junctions": ideal_crossovers,
            "accumulated_twist_degrees": round(accumulated_twist, 2),
            "torsional_strain_energy_pN_nm": torsional_strain_energy,
            "structural_verdict": stability_verdict
        }

class ChronomorphicShannonEntropyEngine:
    r"""
    Chronomorphic Multi-Generational Epigenetic Network Entropy Decay Manifold
    """
    @staticmethod
    def simulate_entropy_manifold(generations: int = 50, base_entropy: float = 0.85, decay_lambda: float = 0.035) -> dict:
        trajectory = []
        h_current = base_entropy
        for gen in range(generations):
            # Multi-compartment epigenetic noise injection
            noise = (random.random() - 0.5) * 0.005
            h_current = base_entropy * math.exp(-decay_lambda * gen) + (0.15 * (1.0 - math.exp(-decay_lambda * gen))) + noise
            if gen % 10 == 0:
                trajectory.append((gen, round(float(h_current), 4)))

        return {
            "simulated_generations": generations,
            "initial_information_fidelity": base_entropy,
            "final_retained_entropy": round(float(h_current), 4),
            "entropy_loss_pct": f"{round((1.0 - (h_current / base_entropy)) * 100.0, 2)}%",
            "generational_decay_trajectory": trajectory
        }
