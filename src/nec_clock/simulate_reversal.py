import math

# ৩টি শীর্ষ স্ক্যাফোল্ডের সিমুলেশন প্যারামিটার
baseline_age = 74.2
baseline_entropy = 0.8924

candidates = [
    {"name": "DREDGE-01 (Hydroxamate Core)", "potency": 0.18},
    {"name": "DREDGE-02 (Salicylate-amide)", "potency": 0.14},
    {"name": "DREDGE-03 (Thiazole-carboxylic)", "potency": 0.10}
]

print("\n=======================================================")
print(f"Sample Actual Age: {baseline_age} years | Baseline NEC: {baseline_age} years")
print(f"Baseline Epigenetic Entropy: {baseline_entropy:.4f} bits")
print("=======================================================")
print(f"{'Candidate':<32} {'Potency':<10} {'Post-Age':<12} {'Delta (Δ)':<12} {'Entropy Drop'}")
print("-" * 75)

for c in candidates:
    potency = c["potency"]
    delta_age = round(baseline_age * potency * 1.54, 1)
    post_age = round(baseline_age - delta_age, 1)
    entropy_drop = round(potency * 0.2288, 4)
    
    print(f"{c['name']:<32} {str(int(potency*100))+'%':<10} {str(post_age)+' yrs':<12} {str(-delta_age)+' yrs':<12} {str(entropy_drop)+' bits'}")

print("=======================================================\n")
