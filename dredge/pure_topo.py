import math

def euclidean_dist(p1, p2):
    return math.sqrt(sum((a-b)**2 for a,b in zip(p1,p2)))

def betti_proxy_entropy(betas, threshold=0.5):
    """Topological complexity ~ number of high-entropy CpGs"""
    return sum(1 for b in betas if abs(b-0.5) < threshold) / len(betas) if betas else 0.0

def persistent_entropy_proxy(distances):
    """Pure proxy for persistent homology entropy"""
    if not distances:
        return 0.0
    total = sum(distances)
    if total == 0:
        return 0.0
    probs = [d/total for d in distances]
    return -sum(p*math.log2(p) for p in probs if p>0)

def dredge_score(mean_H, kinetics, topo):
    """Final DREDGE score = H * K * T"""
    return mean_H * kinetics * (1.0 + topo)
