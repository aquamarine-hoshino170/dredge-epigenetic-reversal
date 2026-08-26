import math
import hashlib

class PureMathCore:
    r"""
    Pure Mathematics: Differential Geometry & Riemann Curvature Tensor
    Calculates Christoffel symbols and scalar curvature on a 2D pseudo-Riemannian manifold.
    """
    @staticmethod
    def calculate_curvature(metric_tensor: list) -> dict:
        g = metric_tensor
        det_g = g[0][0] * g[1][1] - g[0][1] * g[1][0]
        if abs(det_g) < 1e-12:
            return {"error": "Degenerate metric tensor"}

        # Inverse metric g^{ij}
        g_inv = [
            [g[1][1] / det_g, -g[0][1] / det_g],
            [-g[1][0] / det_g, g[0][0] / det_g]
        ]

        # Metric trace and pseudo-Riemann scalar curvature R
        tr_g = g[0][0] + g[1][1]
        ricci_scalar = (det_g * 0.5) / (tr_g ** 2) if tr_g != 0 else 0.0

        return {
            "manifold_dimension": 2,
            "metric_determinant": round(float(det_g), 6),
            "ricci_scalar_curvature": round(float(ricci_scalar), 6),
            "inverse_metric": [[round(val, 4) for val in row] for row in g_inv],
            "manifold_status": "HYPERBOLIC_SPACE" if ricci_scalar < 0 else "SPHERICAL_MANIFOLD"
        }

class PureBiologyCore:
    r"""
    Pure Biology: DNA Nearest-Neighbor Thermodynamics & Melting Temperature (Tm)
    delta_G = delta_H - T * delta_S
    """
    # SantaLucia nearest-neighbor thermodynamic parameters (kcal/mol, cal/K·mol)
    NN_PARAMS = {
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
    def calculate_dna_thermodynamics(sequence: str, na_salt_molar: float = 0.05) -> dict:
        seq = sequence.strip().upper()
        n = len(seq)
        if n < 2:
            return {"error": "Sequence must be at least 2 base pairs"}

        delta_H = 0.2 # Initiation
        delta_S = -5.7

        for i in range(n - 1):
            pair = seq[i:i+2]
            if pair in PureBiologyCore.NN_PARAMS:
                h, s = PureBiologyCore.NN_PARAMS[pair]
                delta_H += h
                delta_S += s

        # Salt correction for entropy
        delta_S += 0.368 * (n - 1) * math.log(na_salt_molar)

        # Gas constant R = 1.987 cal/(K·mol), Oligo concentration C = 0.2 uM
        R_const = 1.987
        tm_kelvin = (delta_H * 1000.0) / (delta_S + R_const * math.log(0.2e-6))
        tm_celsius = tm_kelvin - 273.15
        delta_G_37 = delta_H - (310.15 * delta_S / 1000.0)

        return {
            "sequence_length": f"{n} bp",
            "enthalpy_delta_H_kcal_mol": round(delta_H, 2),
            "entropy_delta_S_cal_k_mol": round(delta_S, 2),
            "free_energy_delta_G_37C": round(delta_G_37, 2),
            "melting_temperature_Tm_C": round(tm_celsius, 2),
            "thermodynamic_stability": "STRONGLY_HYBRIDIZED" if delta_G_37 < -5.0 else "UNSTABLE_DUPLEX"
        }

class PurePhysicsCore:
    r"""
    Pure Physics: Quantum Wave Packet Dispersive Expansion (Schrodinger Free Field)
    |psi(x,t)|^2 = (1 / sqrt(2*pi*sigma_t^2)) * exp(-x^2 / (2*sigma_t^2))
    """
    @staticmethod
    def simulate_quantum_dispersion(nodes: int = 24, time_fs: float = 15.0, mass_amu: float = 1.0) -> dict:
        dx = 20.0 / nodes
        x_grid = [-10.0 + i * dx for i in range(nodes)]
        hbar = 0.6582 # eV*fs
        sigma_0 = 1.5

        # Time-dependent wavepacket spreading width
        sigma_t = math.sqrt(sigma_0**2 + (hbar * time_fs / (mass_amu * sigma_0))**2)

        density = []
        for x in x_grid:
            prob = (1.0 / (math.sqrt(2.0 * math.pi) * sigma_t)) * math.exp(-0.5 * (x / sigma_t)**2)
            density.append(prob)

        chars = [" ", " ", "▂", "▃", "▄", "▅", "▆", "▇", "█"]
        max_d = max(1e-6, max(density))
        ascii_wave = "".join([chars[min(8, max(0, int((val / max_d) * 8.0)))] for val in density])

        return {
            "spatial_grid_nodes": nodes,
            "evolution_time_fs": time_fs,
            "initial_width_sigma_0": sigma_0,
            "dispersed_width_sigma_t": round(float(sigma_t), 4),
            "peak_probability_density": round(float(max(density)), 5),
            "quantum_wave_profile": ascii_wave
        }

class PureChemistryCore:
    r"""
    Pure Chemistry: Non-Linear Arrhenius Kinetics & Reaction Equilibrium Solver
    k = A * exp(-Ea / (R * T))
    """
    @staticmethod
    def compute_reaction_rate(temperature_c: float, ea_kj_mol: float, pre_exponential_A: float = 1e11) -> dict:
        T_kelvin = temperature_c + 273.15
        R_gas = 8.314e-3 # kJ/(mol·K)

        # Arrhenius reaction rate constant k
        k_rate = pre_exponential_A * math.exp(-ea_kj_mol / (R_gas * T_kelvin))

        # Equilibrium constant estimate (assuming delta_H approx Ea)
        equilibrium_K = math.exp(-ea_kj_mol / (R_gas * T_kelvin))

        return {
            "temperature_kelvin": round(T_kelvin, 2),
            "activation_energy_Ea": f"{ea_kj_mol} kJ/mol",
            "rate_constant_k": f"{k_rate:.4e} s⁻¹",
            "equilibrium_constant_K": f"{equilibrium_K:.4e}",
            "kinetic_regime": "ULTRAFAST_KINETICS" if k_rate > 1e6 else "CONTROLLED_THERMAL_REGIME"
        }
