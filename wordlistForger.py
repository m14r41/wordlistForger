#!/usr/bin/env python3
import argparse
import random
import string
import sys
import time
from math import prod
VERSION = "1.0.4"

# =========================
# Colors
# =========================
class C:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    DIM = "\033[2m"

# =========================
# Banner
# =========================
BANNER = (
    f"{C.CYAN}╔══════════════════════════╗\n"
    f"║ wordlistForger by M14R41 ║\n"
    f"╚══════════════════════════╝{C.RESET}"
)

# BANNER = f"{C.CYAN}WordlistForge v2 by M14R41{C.RESET}"
# =========================
# Pools
# =========================
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGIT = string.digits
HEX   = "0123456789abcdef"

# =========================
# Logger
# =========================
def info(msg): print(f"[+] {msg}")
def ok(msg): print(f"{C.GREEN}[+]{C.RESET} {msg}")
def err(msg): print(f"{C.RED}[-]{C.RESET} {msg}")

# =========================
# Core Logic
# =========================
def get_pool(ch, strict_case, match_pattern=False):
    if match_pattern:
        if ch == 'x': return HEX
        if ch == 'n': return DIGIT
        if ch == 'a': return LOWER
        if ch == 'A': return UPPER
        return ch

    if ch.isdigit():
        return DIGIT
    if ch.isalpha():
        return LOWER if strict_case and ch.islower() else (UPPER if strict_case else LOWER + UPPER)

    return ch


def count_combinations(pattern, lock, lock_mask, strict_case, match_pattern):
    sizes = []
    i = 0
    while i < len(pattern):
        if lock and pattern.startswith(lock, i):
            sizes.append(1)
            i += len(lock)
            continue

        if lock_mask and i < len(lock_mask) and lock_mask[i] != "x":
            sizes.append(1)
        else:
            pool = get_pool(pattern[i], strict_case, match_pattern)
            sizes.append(len(pool) if isinstance(pool, str) else 1)

        i += 1
    return prod(sizes)


def generate_word(pattern, lock, lock_mask, strict_case, match_pattern):
    out = []
    i = 0
    while i < len(pattern):
        if lock and pattern.startswith(lock, i):
            out.append(lock)
            i += len(lock)
            continue

        if lock_mask and i < len(lock_mask) and lock_mask[i] != "x":
            out.append(lock_mask[i])
        else:
            pool = get_pool(pattern[i], strict_case, match_pattern)
            out.append(random.choice(pool) if isinstance(pool, str) else str(pool))

        i += 1
    return "".join(out)

# =========================
# PROGRESS BAR
# =========================
def progress(current, total, start_time):
    percent = current / total
    bar_len = 25

    filled = int(bar_len * percent)

    bar = ""
    for i in range(bar_len):
        if i < filled:
            if percent < 0.5:
                bar += f"{C.GREEN}▰"
            elif percent < 0.8:
                bar += f"{C.YELLOW}▰"
            else:
                bar += f"{C.RED}▰"
        else:
            bar += f"{C.DIM}▱"

    elapsed = time.time() - start_time
    speed = current / elapsed if elapsed > 0 else 0
    eta = (total - current) / speed if speed > 0 else 0

    sys.stdout.write(
        f"\r{bar}{C.RESET} "
        f"{percent*100:5.1f}% "
        f"{current}/{total} "
        f"| {speed:,.0f} w/s "
        f"| ETA {eta:,.1f}s"
    )
    sys.stdout.flush()

# =========================
# MAIN
# =========================
def main():
    print(BANNER)

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pattern", required=True)
    parser.add_argument("-l", "--limit", type=int, required=True)
    parser.add_argument("--lock")
    parser.add_argument("--lock-mask")
    parser.add_argument("--strict-case", action="store_true")
    parser.add_argument("--match-pattern", action="store_true")
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("-o", "--output", default="wordlist.txt")
    parser.add_argument("--live", action="store_true")
    parser.add_argument("-v", "--version", action="version", version=f"wordlistForger : {VERSION}")


    args = parser.parse_args()

    start = time.time()

    # =========================
    # INFO  
    # =========================
    info("starting engine")
    
    if args.seed:
        random.seed(args.seed)

    if args.lock_mask and len(args.lock_mask) != len(args.pattern):
        err("lock-mask mismatch")
        sys.exit(1)

    info("calculating space...")

    max_possible = count_combinations(
        args.pattern,
        args.lock,
        args.lock_mask,
        args.strict_case,
        args.match_pattern
    )

    info(f"max possible: {max_possible}")

    if args.limit > max_possible:
        err("limit exceeds possible combinations")
        sys.exit(1)

    info("generating...")

    results = set()
    counter = 0

    try:
        while len(results) < args.limit:
            word = generate_word(
                args.pattern,
                args.lock,
                args.lock_mask,
                args.strict_case,
                args.match_pattern
            )

            if word not in results:
                results.add(word)
                counter += 1

                if args.live:
                    print(word)
                else:
                    progress(counter, args.limit, start)

    except KeyboardInterrupt:
        print(f"\n{C.RED}[!]{C.RESET} stopped by user")
        print(f"{C.YELLOW}[~]{C.RESET} saving...")

    print()

    with open(args.output, "w") as f:
        for w in results:
            f.write(w + "\n")

    elapsed = time.time() - start
    speed = len(results) / elapsed if elapsed > 0 else 0

    ok(f"generated: {len(results)}")
    ok(f"speed: {speed:,.2f} w/s")
    ok(f"time: {elapsed:.2f}s")
    ok(f"saved: {args.output}")

if __name__ == "__main__":
    main()
