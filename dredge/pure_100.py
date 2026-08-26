import math

# ===== 1. MATHEMATICS (20) =====
def f001_pythagoras(a,b): return math.sqrt(a*a + b*b)
def f002_circle_area(r): return math.pi*r*r
def f003_sphere_volume(r): return 4/3*math.pi*r**3
def f004_quadratic_root(a,b,c): return (-b + math.sqrt(b*b-4*a*c))/(2*a) if b*b>=4*a*c else None
def f005_logistic(x): return 1/(1+math.exp(-x))
def f006_factorial(n): return math.factorial(n)
def f007_fib(n): a,b=0,1; [exec("a,b=b,a+b") for _ in range(n)]; return a
def f008_gcd(a,b): return math.gcd(a,b)
def f009_lcm(a,b): return abs(a*b)//math.gcd(a,b) if a and b else 0
def f010_mean(arr): return sum(arr)/len(arr) if arr else 0
def f011_std(arr): m=sum(arr)/len(arr) if arr else 0; return math.sqrt(sum((x-m)**2 for x in arr)/len(arr)) if arr else 0
def f012_entropy(p): return -sum(x*math.log2(x) for x in p if x>0) if p else 0
def f013_sigmoid_deriv(x): s=1/(1+math.exp(-x)); return s*(1-s)
def f014_sin_deg(d): return math.sin(math.radians(d))
def f015_distance_3d(p1,p2): return math.sqrt(sum((a-b)**2 for a,b in zip(p1,p2)))
def f016_triangle_area(a,b,c): s=(a+b+c)/2; return math.sqrt(max(s*(s-a)*(s-b)*(s-c),0))
def f017_compound_interest(p,r,t): return p*(1+r)**t
def f018_prime_check(n): return n>1 and all(n%i for i in range(2,int(n**0.5)+1))
def f019_binom_coeff(n,k): return math.comb(n,k)
def f020_euler_e(x): return math.exp(x)

# ===== 2. PHYSICS (20) =====
def f021_E_mc2(m): return m*299792458**2
def f022_F_ma(m,a): return m*a
def f023_kinetic_energy(m,v): return 0.5*m*v*v
def f024_potential_energy(m,g,h): return m*g*h
def f025_momentum(m,v): return m*v
def f026_pressure(F,A): return F/A if A else 0
def f027_density(m,V): return m/V if V else 0
def f028_ohms_law(I,R): return I*R
def f029_power_W(V,I): return V*I
def f030_wave_speed(f,lam): return f*lam
def f031_gravitational_force(m1,m2,r): return 6.674e-11*m1*m2/(r*r) if r else 0
def f032_escape_velocity(M,R): return math.sqrt(2*6.674e-11*M/R) if R else 0
def f033_time_dilation(t,v): return t/math.sqrt(1-(v/299792458)**2) if v<299792458 else 0
def f034_photon_energy(f): return 6.626e-34*f
def f035_ideal_gas_P(n,T,V): return n*8.314*T/V if V else 0
def f036_half_life(N0,t,T): return N0*0.5**(t/T) if T else 0
def f037_doppler(f,v): return f*(343/(343+v)) if v!=-343 else 0
def f038_lens_power(f): return 1/f if f else 0
def f039_work(F,d): return F*d
def f040_efficiency(Wout,Win): return Wout/Win*100 if Win else 0

# ===== 3. CHEMISTRY (20) =====
def f041_molarity(moles,V): return moles/V if V else 0
def f042_pH(H): return -math.log10(H) if H>0 else 0
def f043_michaelis_menten(S,Vmax,Km): return Vmax*S/(Km+S) if Km+S else 0
def f044_hill(S,Vmax,Kd,n): return Vmax*S**n/(Kd**n+S**n) if Kd**n+S**n else 0
def f045_arrhenius(A,Ea,T): return A*math.exp(-Ea/(8.314*T)) if T else 0
def f046_moles(mass,M): return mass/M if M else 0
def f047_dilution(C1,V1,V2): return C1*V1/V2 if V2 else 0
def f048_gibbs(H,S,T): return H - T*S
def f049_equilibrium_K(dG,T): return math.exp(-dG/(8.314*T)) if T else 0
def f050_bond_energy(bonds): return sum(bonds)
def f051_IC50_inhib(I,IC50): return 1/(1+I/IC50) if IC50 else 0
def f052_solubility(Ksp): return math.sqrt(Ksp)
def f053_rate_constant(k0,T): return k0*math.exp(-1000/T) if T else 0
def f054_mass_percent(solute,solution): return solute/solution*100 if solution else 0
def f055_avogadro_moles(N): return N/6.022e23
def f056_pKa(Ka): return -math.log10(Ka) if Ka>0 else 0
def f057_buffer_pH(pKa,base,acid): return pKa+math.log10(base/acid) if acid and base>0 else 0
def f058_reaction_quotient(Q): return Q
def f059_activation_energy(k1,k2,T1,T2): return 8.314*math.log(k2/k1)/(1/T1-1/T2) if T1!=T2 and k1>0 and k2>0 else 0
def f060_molar_mass(formula_weight): return formula_weight

# ===== 4. BIOLOGY (20) =====
def f061_H_entropy(beta): return -beta*math.log2(beta)-(1-beta)*math.log2(1-beta) if 0<beta<1 else 0
def f062_hardy_weinberg(p): return p*p, 2*p*(1-p), (1-p)*(1-p)
def f063_population_growth(N0,r,t): return N0*math.exp(r*t)
def f064_bmi(w,h): return w/(h*h) if h else 0
def f065_bsa(w,h): return math.sqrt(w*h/3600)
def f066_gfr(age,creat): return 186*(creat**-1.154)*(age**-0.203) if creat and age else 0
def f067_tet2_score(conc,EC50=0.5): return conc/(EC50+conc)
def f068_dredge_score(H,K,T): return H*K*(1+T)
def f069_cell_doubling(N0,td,t): return N0*2**(t/td) if td else 0
def f070_gc_content(seq): return (seq.count('G')+seq.count('C'))/len(seq)*100 if seq else 0
def f071_melting_temp(A,T,G,C): return 2*(A+T)+4*(G+C)
def f072_enzyme_eff(kcat,Km): return kcat/Km if Km else 0
def f073_ld50(dose): return dose
def f074_heart_rate(RR): return 60/RR if RR else 0
def f075_alveolar_gas(P): return P
def f076_blood_volume(w): return w*70
def f077_insulin_dose(glucose): return max(0,(glucose-100)/40)
def f078_mitotic_index(m,t): return m/t*100 if t else 0
def f079_carrying_capacity(r,K,N): return r*N*(1-N/K) if K else 0
def f080_mutation_rate(muts,bases): return muts/bases if bases else 0

# ===== 5. GEOMETRY/TOPOLOGY/ADVANCE (20) =====
def f081_euclidean(a,b): return math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))
def f082_manhattan(a,b): return sum(abs(x-y) for x,y in zip(a,b))
def f083_dot(a,b): return sum(x*y for x,y in zip(a,b))
def f084_cross_2d(a,b): return a[0]*b[1]-a[1]*b[0]
def f085_angle_between(a,b): return math.acos(max(-1,min(1,sum(x*y for x,y in zip(a,b))/(math.sqrt(sum(x*x for x in a))*math.sqrt(sum(y*y for y in b)))))) if a and b else 0
def f086_betti_proxy(betas,thr=0.5): return sum(1 for b in betas if abs(b-0.5)<thr)/len(betas) if betas else 0
def f087_persistent_entropy(dists): s=sum(dists); return -sum((d/s)*math.log2(d/s) for d in dists if d>0 and s>0) if dists else 0
def f088_fractal_dim(N,r): return math.log(N)/math.log(1/r) if r and N>0 and r!=1 else 0
def f089_mandelbrot_iter(c,max_iter=100): z=0; [exec("z=z*z+c") or True for _ in range(max_iter) if abs(z)<=2]; return abs(z)
def f090_lorenz_x(x,y,s=10): return s*(y-x)
def f091_rsa_encrypt(m,e,n): return pow(m,e,n)
def f092_hash_simple(s): return sum(ord(c)* (i+1) for i,c in enumerate(s)) % 100000
def f093_golden_ratio(n): a,b=0,1; [exec("a,b=b,a+b") for _ in range(n)]; return b/a if a else 0
def f094_euler_phi(n): return sum(1 for i in range(1,n+1) if math.gcd(i,n)==1)
def f095_fourier_1(x): return math.sin(x)+0.5*math.sin(2*x)
def f096_chaos_logistic(x,r=3.9): return r*x*(1-x)
def f097_kmeans_dist(x,c): return (x-c)**2
def f098_gradient_descent(x,lr=0.01): return x-lr*2*x
def f099_svd_proxy(a): return math.sqrt(sum(x*x for x in a))
def f100_universe_score(): return 42

def list_all(): return [f"f{i:03d}" for i in range(1,101)]
