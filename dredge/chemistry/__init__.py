import math

class ChemistryCore:
    """Real Chemical Kinetics, Thermodynamics & Electrochemical Models"""
    @staticmethod
    def arrhenius_rate(temp_c: float = 25.0, ea_kj: float = 50.0, a_factor: float = 1e11) -> dict:
        T_k = temp_c + 273.15
        k = a_factor * math.exp(-ea_kj / (8.314e-3 * T_k))
        return {"temp_K": round(T_k, 2), "rate_constant_k": f"{k:.4e} s⁻¹"}

    @staticmethod
    def nernst_redox(e0_v: float = 1.10, n_electrons: int = 2, q_ratio: float = 0.01, temp_c: float = 25.0) -> dict:
        T_k = temp_c + 273.15
        e_cell = e0_v - (8.314 * T_k / (n_electrons * 96485.0)) * math.log(q_ratio)
        return {"standard_E0": e0_v, "equilibrium_Q": q_ratio, "E_cell_V": round(e_cell, 4)}

    @staticmethod
    def ideal_vs_real_gas(p_atm: float = 50.0, temp_c: float = 25.0) -> dict:
        T_k = temp_c + 273.15
        R = 0.08206
        vm = R * T_k / p_atm
        return {"pressure_atm": p_atm, "molar_volume_L": round(vm, 4)}
