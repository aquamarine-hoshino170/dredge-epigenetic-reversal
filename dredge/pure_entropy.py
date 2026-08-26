import math
def H(beta: float) -> float:
    if beta <= 0.0 or beta >= 1.0:
        return 0.0
    return -beta * math.log2(beta) - (1.0 - beta) * math.log2(1.0 - beta)
def H_list(betas):
    return [H(b) for b in betas]
def mean_entropy(betas):
    if not betas:
        return 0.0
    return sum(H_list(betas)) / len(betas)
def delta_age_from_entropy(h_old, h_new, factor=27.1):
    return (h_new - h_old) * factor
