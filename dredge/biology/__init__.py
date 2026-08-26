import math

class BiologyCore:
    """Real Thermodynamic & Enzyme Kinetics Formalisms"""
    NN_PARAMS = {
        'AA': (-7.6, -21.3), 'TT': (-7.6, -21.3), 'AT': (-7.2, -20.4), 'TA': (-7.2, -21.3),
        'CA': (-8.5, -22.7), 'TG': (-8.5, -22.7), 'GT': (-8.4, -22.4), 'AC': (-8.4, -22.4),
        'CT': (-7.8, -21.0), 'AG': (-7.8, -21.0), 'GA': (-8.2, -22.2), 'TC': (-8.2, -22.2),
        'CG': (-10.6, -27.2), 'GC': (-9.8, -24.4), 'GG': (-8.0, -19.9), 'CC': (-8.0, -19.9)
    }

    @staticmethod
    def dna_thermodynamics(sequence: str = "GCATGCATGC", salt_molar: float = 0.05) -> dict:
        seq = sequence.strip().upper()
        n = len(seq)
        if n < 2: return {"error": "Sequence too short"}
        dH, dS = 0.2, -5.7
        for i in range(n - 1):
            pair = seq[i:i+2]
            if pair in BiologyCore.NN_PARAMS:
                h, s = BiologyCore.NN_PARAMS[pair]
                dH += h; dS += s
        dS += 0.368 * (n - 1) * math.log(salt_molar)
        tm = (dH * 1000.0) / (dS + 1.987 * math.log(0.2e-6)) - 273.15
        dG = dH - (310.15 * dS / 1000.0)
        return {"sequence_len": n, "dH_kcal_mol": round(dH, 2), "dG_37C_kcal_mol": round(dG, 2), "Tm_C": round(tm, 2)}

    @staticmethod
    def michaelis_menten(s: float = 5.0, vmax: float = 100.0, km: float = 2.0) -> dict:
        v = (vmax * s) / (km + s)
        return {"substrate_conc": s, "velocity_v": round(v, 4), "saturation_pct": round((s / (km + s)) * 100.0, 2)}
