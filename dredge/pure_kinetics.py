import math

def michaelis_menten(S, Vmax, Km):
    """V = Vmax * S / (Km + S)"""
    if Km + S == 0:
        return 0.0
    return Vmax * S / (Km + S)

def hill_equation(S, Vmax, Kd, n):
    """Hill: V = Vmax * S^n / (Kd^n + S^n)"""
    Sn = math.pow(S, n)
    Kdn = math.pow(Kd, n)
    if Kdn + Sn == 0:
        return 0.0
    return Vmax * Sn / (Kdn + Sn)

def inhibition_curve(I, IC50, n=1.0):
    """Fractional activity: 1 / (1 + (I/IC50)^n)"""
    if IC50 == 0:
        return 0.0
    return 1.0 / (1.0 + math.pow(I / IC50, n))

def tet2_reactivation_score(drug_conc, EC50=0.5, Emax=1.0):
    """Your TET2 allosteric activation"""
    return Emax * drug_conc / (EC50 + drug_conc)

def kinetics_list(func, conc_list, *args):
    return [func(c, *args) for c in conc_list]
