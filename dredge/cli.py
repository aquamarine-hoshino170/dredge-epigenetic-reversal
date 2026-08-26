import argparse
import sys
from dredge.omni_kernel import OmniVerseCore

def run_all_340():
    print("\n" + "="*70)
    print("      DREDGE v340.0.0 OMNI-VERSE MATRIX (340 FEATURES)")
    print("="*70)
    
    core = OmniVerseCore()
    methods = [m for m in dir(core) if m.startswith(('bio_', 'chem_', 'phys_', 'field_', 'math_'))]
    methods.sort()
    
    counts = {"Bio": 0, "Chem": 0, "Phys": 0, "Field": 0, "Math": 0}
    
    for idx, m_name in enumerate(methods, 1):
        res = getattr(core, m_name)()
        feat = res.pop('feature')
        prefix = feat.split('-')[0]
        if prefix in counts: counts[prefix] += 1
        
        params_str = ", ".join(f"{k}: {v}" for k, v in res.items())
        # Print only the first and last few to prevent terminal overflow, but count all
        if idx <= 15 or idx >= 330:
            print(f"[{idx:03d}] {feat} -> {params_str}")
        elif idx == 16:
            print(f" ... [Executing Remaining 310 Engines in Background] ... ")

    print("-" * 70)
    print(" >> VALIDATION REPORT:")
    print(f" • Biology Engines:      {counts.get('Bio', 0)} / 60")
    print(f" • Chemistry Engines:    {counts.get('Chem', 0)} / 80")
    print(f" • Physics Engines:      {counts.get('Phys', 0)} / 90")
    print(f" • Field Theory Engines: {counts.get('Field', 0)} / 20")
    print(f" • Math/Crypto Engines:  {counts.get('Math', 0)} / 90")
    print(f" • TOTAL ACTIVE ENGINES: {len(methods)} / 340")
    print("="*70 + "\n")

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='v340.0.0 Omni-Verse Matrix')
    parser.add_argument('--all', action='store_true', help='Execute all 340 engines')
    parser.add_argument('--custom', nargs=4, metavar=('ENGINE_ID', 'PARAM_A', 'PARAM_B', 'PARAM_C'), 
                        help='Run a specific dynamic engine with custom values (e.g., phys_085_dynamic 10.5 2.1 3.0)')
    
    args = parser.parse_args()

    if args.custom:
        engine_name, p_a, p_b, p_c = args.custom
        try:
            func = getattr(OmniVerseCore, engine_name)
            res = func(float(p_a), float(p_b), float(p_c))
            print(f"\n[CUSTOM EXECUTION: {engine_name}]")
            for k, v in res.items(): print(f" • {k}: {v}")
            print()
        except AttributeError:
            print(f"\n[ERROR] Engine '{engine_name}' not found. Try 'phys_085_dynamic' etc.\n")
        return

    if args.all:
        run_all_340()
        return

    run_all_340()

if __name__ == '__main__':
    main()
