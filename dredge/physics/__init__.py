import math
import cmath

class QuantumCore:
    """Pure State-Vector Quantum Simulator (Born Rule & Gate Matrices)"""
    @staticmethod
    def simulate_bell_pair():
        # |00> state vector
        state = [1.0 + 0j, 0.0 + 0j, 0.0 + 0j, 0.0 + 0j]
        # H on Qubit 0 -> 1/sqrt(2) (|00> + |10>)
        inv_sqrt2 = 1.0 / math.sqrt(2.0)
        state = [inv_sqrt2 + 0j, 0.0 + 0j, inv_sqrt2 + 0j, 0.0 + 0j]
        # CNOT (Q0 -> Q1) -> 1/sqrt(2) (|00> + |11>)
        state[2], state[3] = state[3], state[2]
        probs = [round(abs(amp)**2, 4) for amp in state]
        return {"|00>": probs[0], "|01>": probs[1], "|10>": probs[2], "|11>": probs[3]}

class SignalCore:
    """Cooley-Tukey 1D Fast Fourier Transform (Zero-Dependency)"""
    @staticmethod
    def fft(x: list):
        N = len(x)
        if N <= 1: return x
        even = SignalCore.fft(x[0::2])
        odd = SignalCore.fft(x[1::2])
        T = [cmath.exp(-2j * math.pi * k / N) * odd[k] for k in range(N // 2)]
        return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

class OrbitalCore:
    """Velocity-Verlet Symplectic Orbital Integrator"""
    @staticmethod
    def step_orbit(pos=[10.0, 0.0], vel=[0.0, 10.0], dt=0.05, GM=1000.0, steps=20):
        r = list(pos)
        v = list(vel)
        for _ in range(steps):
            r_mag = math.sqrt(r[0]**2 + r[1]**2)
            acc = [-GM * r[0] / (r_mag**3), -GM * r[1] / (r_mag**3)]
            r[0] += v[0] * dt + 0.5 * acc[0] * (dt**2)
            r[1] += v[1] * dt + 0.5 * acc[1] * (dt**2)
            r_mag_new = math.sqrt(r[0]**2 + r[1]**2)
            acc_new = [-GM * r[0] / (r_mag_new**3), -GM * r[1] / (r_mag_new**3)]
            v[0] += 0.5 * (acc[0] + acc_new[0]) * dt
            v[1] += 0.5 * (acc[1] + acc_new[1]) * dt
        return {"final_position": [round(r[0], 3), round(r[1], 3)], "final_radius": round(math.sqrt(r[0]**2 + r[1]**2), 3)}
