import sys
import readline
from dredge.bio_kernel import (
    UniversalBioKernel,
    BioVirtualFileSystemPOSIX,
    BioSystemMonitorAndSignals,
    LinuxBioSyscallAndLKM,
    LucasRuthlessQCEngine,
    NativeAssemblyBitKernel
)

def start_interactive_shell():
    print("""
============================================================================
  🐧 AQUAMARINE DREDGE MONOLITH: PURE LINUX-BIO REPL SHELL (v27.0.0)
============================================================================
  * Ring-0 Protected Mode Active. VFS mounted on /bio. PID 1 init running.
  * Type 'help' for built-in syscalls, 'exit' to halt the kernel.
============================================================================
""")
    while True:
        try:
            cmd_line = input("dredge-kernel:root# ").strip()
            if not cmd_line:
                continue
            parts = cmd_line.split()
            cmd = parts[0].lower()
            args = parts[1:]

            if cmd in ["exit", "halt", "poweroff"]:
                print("[+] Halting Bio-Kernel... System going down.")
                break
            elif cmd == "help":
                print("""
Available Kernel Commands:
  • ls /bio           : List biological VFS nodes
  • cat <node>        : Read biological VFS node (e.g. cat /bio/sys/atp_pool)
  • top               : Real-time cellular task monitor
  • kill -9 <pid>     : Dispatch apoptotic signal to cellular thread
  • syscall <name>    : Execute Bio-Syscall (bio_fork, bio_mmap, bio_ptrace)
  • lsmod             : List loaded biological kernel modules (LKM)
  • insmod <mod>      : Insert synthetic plasmid kernel module
  • rmmod <mod>       : Remove synthetic kernel module
  • audit <dna>       : Lucas ruthless code auditor & purge
  • scan <dna>        : 2-bit native assembly high-speed scan
""")
            elif cmd == "ls" and args and args[0] == "/bio":
                for node in BioVirtualFileSystemPOSIX.ls_nodes():
                    print(f"  [r--r--r-- bio bio] {node}")
            elif cmd == "cat" and args:
                print(BioVirtualFileSystemPOSIX.cat_node(args[0]))
            elif cmd == "top":
                print(BioSystemMonitorAndSignals.render_bio_top())
            elif cmd == "kill" and len(args) >= 2 and args[0] == "-9":
                res = BioSystemMonitorAndSignals.send_cellular_signal(int(args[1]), 9)
                print(f"[✓] {res['dispatched_signal']} sent to PID {res['target_cellular_pid']}")
            elif cmd == "syscall" and args:
                arg_val = args[1] if len(args) > 1 else ""
                res = LinuxBioSyscallAndLKM.execute_syscall(args[0], arg_val)
                for k, v in res.items():
                    print(f"  {k}: {v}")
            elif cmd == "lsmod":
                res = LinuxBioSyscallAndLKM.manage_lkm("lsmod")
                print("  Module Name          Size (KB)  Status")
                print("  " + "-"*50)
                for m, info in res['loaded_kernel_modules'].items():
                    print(f"  {m:<20} {info['memory_kb']:<10} {info['status']}")
            elif cmd == "insmod" and args:
                print(LinuxBioSyscallAndLKM.manage_lkm("insmod", args[0])['lkm_action'])
            elif cmd == "rmmod" and args:
                print(LinuxBioSyscallAndLKM.manage_lkm("rmmod", args[0])['lkm_action'])
            elif cmd == "audit" and args:
                res = LucasRuthlessQCEngine.audit_and_purge(args[0])
                print(f"  Lucas Verdict: {res['verdict']}")
                print(f"  Purged DNA   : {res['purged_repaired_dna']}")
            elif cmd == "scan" and args:
                res = NativeAssemblyBitKernel.ultra_fast_bit_scan(args[0])
                print(f"  Latency: {res['execution_latency']} | Throughput: {res['processing_throughput']}")
            else:
                print(f"dredge-sh: command not found: {cmd}. Type 'help' for commands.")
        except (KeyboardInterrupt, EOFError):
            print("\n[+] Kernel Interrupt received. Exiting.")
            break
