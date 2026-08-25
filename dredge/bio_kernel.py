import numpy as np
import math
import hashlib
import time
import asyncio
import random

class AsyncP2PBioLedgerEngine:
    r"""
    Asynchronous Non-Blocking P2P Bio-Consensus Ledger via Proof-of-Sequence
    """
    @staticmethod
    async def _mine_block_async(index: int, prev_hash: str, mutation_data: str, node_id: int, latency_ms: float = 10.0) -> dict:
        await asyncio.sleep(latency_ms / 1000.0)
        nonce = 0
        target_prefix = "0"
        ts = time.time()
        while True:
            payload = f"{index}{prev_hash}{mutation_data}{ts}{nonce}{node_id}"
            h = hashlib.sha256(payload.encode('utf-8')).hexdigest()
            if h.startswith(target_prefix):
                return {
                    "block_index": index,
                    "mined_by_node": node_id,
                    "timestamp": round(ts, 2),
                    "mutation_payload": mutation_data,
                    "previous_hash": prev_hash,
                    "block_hash": h,
                    "nonce": nonce
                }
            nonce += 1

    @staticmethod
    def run_consensus_mesh(mutations: list, num_nodes: int = 3) -> dict:
        async def main_mesh():
            chain = [{
                "block_index": 0,
                "mined_by_node": 0,
                "timestamp": round(time.time(), 2),
                "mutation_payload": "GENESIS_ROOT_EPIGENOME",
                "previous_hash": "0"*64,
                "block_hash": hashlib.sha256(b"GENESIS").hexdigest(),
                "nonce": 0
            }]
            for idx, mut in enumerate(mutations, 1):
                prev_h = chain[-1]["block_hash"]
                # Explicitly wrap coroutines into asyncio Tasks for Python 3.14+ compatibility
                tasks = [
                    asyncio.create_task(
                        AsyncP2PBioLedgerEngine._mine_block_async(idx, prev_h, mut, node, latency_ms=random.uniform(5.0, 20.0))
                    )
                    for node in range(num_nodes)
                ]
                # First task to complete wins consensus
                done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
                for task in pending:
                    task.cancel()
                    try:
                        await task
                    except asyncio.CancelledError:
                        pass
                mined_block = list(done)[0].result()
                chain.append(mined_block)
            return chain

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result_chain = loop.run_until_complete(main_mesh())
        loop.close()
        return {
            "total_blocks": len(result_chain),
            "participating_nodes": num_nodes,
            "chain_ledger": result_chain
        }

class QuantumLindbladDensityVisualizerEngine:
    @staticmethod
    def simulate_and_visualize(sites: int = 4, total_time_fs: float = 40.0, dt_fs: float = 1.0, dephasing_rate: float = 0.01) -> dict:
        H = np.zeros((sites, sites), dtype=complex)
        for i in range(sites):
            H[i, i] = 12100.0 + i * 120.0
            if i < sites - 1:
                H[i, i+1] = -75.0
                H[i+1, i] = -75.0
        H /= 1000.0

        rho = np.zeros((sites, sites), dtype=complex)
        rho[0, 0] = 1.0

        steps = int(total_time_fs / dt_fs)
        for _ in range(steps):
            d_rho = -1j * (H @ rho - rho @ H)
            for i in range(sites):
                for j in range(sites):
                    if i != j:
                        d_rho[i, j] -= dephasing_rate * rho[i, j]
            rho += d_rho * (dt_fs / 10.0)
            rho /= np.trace(rho)

        chars = [" ", "·", "x", "#"]
        matrix_ascii = []
        for r in range(sites):
            row_str = ""
            for c in range(sites):
                mag = abs(rho[r, c])
                idx = min(3, max(0, int(mag * 3.5)))
                row_str += f"[{chars[idx]}] "
            matrix_ascii.append(row_str.strip())

        return {
            "sites": sites,
            "site_populations": [round(float(rho[i, i].real), 4) for i in range(sites)],
            "max_cross_coherence": round(float(np.max(np.abs(rho - np.diag(np.diag(rho))))), 5),
            "density_matrix_ascii": matrix_ascii
        }

class TuringMorphogenesisDynamicGridEngine:
    @staticmethod
    def render_morphogenesis(grid_size: int = 20, iterations: int = 80) -> dict:
        np.random.seed(42)
        u = np.ones((grid_size, grid_size)) + 0.05 * np.random.randn(grid_size, grid_size)
        v = np.zeros((grid_size, grid_size)) + 0.05 * np.random.randn(grid_size, grid_size)

        center = grid_size / 2.0
        mask = np.zeros((grid_size, grid_size), dtype=bool)
        for r in range(grid_size):
            for c in range(grid_size):
                if math.sqrt((r - center)**2 + (c - center)**2) <= (grid_size / 2.0 - 1.0):
                    mask[r, c] = True

        Du, Dv = 0.16, 0.08
        F, k = 0.035, 0.065
        dt = 1.0

        for _ in range(iterations):
            lap_u = (np.roll(u, 1, 0) + np.roll(u, -1, 0) + np.roll(u, 1, 1) + np.roll(u, -1, 1) - 4 * u)
            lap_v = (np.roll(v, 1, 0) + np.roll(v, -1, 0) + np.roll(v, 1, 1) + np.roll(v, -1, 1) - 4 * v)
            uvv = u * v * v
            u += dt * (Du * lap_u - uvv + F * (1.0 - u))
            v += dt * (Dv * lap_v + uvv - (F + k) * v)
            u[~mask] = 0.0
            v[~mask] = 0.0

        chars = [" ", "·", "x", "#"]
        render = []
        for r in range(grid_size):
            line = "".join([chars[min(3, max(0, int(u[r, c] * 3.0)))] if mask[r, c] else " " for c in range(grid_size)])
            render.append(line)

        return {
            "grid_dimensions": f"{grid_size}x{grid_size}",
            "active_tissue_area_pct": f"{round((np.sum(mask)/(grid_size**2))*100.0, 2)}%",
            "mean_activator_density": round(float(np.mean(u[mask])), 4),
            "ascii_tissue_render": render
        }

class DNAOrigamiTorsionRouterEngine:
    @staticmethod
    def calculate_routing_strain(scaffold_bp: int, staple_strands: int, target_planes: int = 3) -> dict:
        turns = scaffold_bp / 10.5
        ideal_crossovers = int(turns * 1.5 * (target_planes / 2.0))
        twist_deviation = (scaffold_bp * 34.28) % 360.0
        strain_energy_pN_nm = round(0.5 * 0.04 * (twist_deviation ** 2) * (target_planes / 2.0), 2)

        return {
            "scaffold_length_bp": scaffold_bp,
            "staple_strands_routed": staple_strands,
            "spatial_target_planes": target_planes,
            "optimal_crossovers": ideal_crossovers,
            "accumulated_twist_deg": round(twist_deviation, 2),
            "torsion_strain_energy_pN_nm": strain_energy_pN_nm,
            "stability_status": "HIGH_RIGIDITY_NANO_STRUCTURE" if strain_energy_pN_nm < 800.0 else "SHEAR_STRAIN_LIMIT_EXCEEDED"
        }

class ChronomorphicShannonManifoldEngine:
    @staticmethod
    def simulate_entropy_manifold(generations: int = 50, base_entropy: float = 0.92, decay_constant: float = 0.028) -> dict:
        trajectory = []
        h = base_entropy
        for g in range(generations):
            noise = (random.random() - 0.5) * 0.003
            h = base_entropy * math.exp(-decay_constant * g) + 0.12 * (1.0 - math.exp(-decay_constant * g)) + noise
            if g % 10 == 0:
                trajectory.append((g, round(float(h), 4)))

        return {
            "generations_simulated": generations,
            "initial_shannon_fidelity": base_entropy,
            "final_retained_entropy": round(float(h), 4),
            "entropy_loss_pct": f"{round((1.0 - (h / base_entropy)) * 100.0, 2)}%",
            "decay_trajectory": trajectory
        }
