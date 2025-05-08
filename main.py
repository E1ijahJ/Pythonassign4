"""
Multithreaded vs Single-threaded Runtime (Range: 1 to 100000):
- Single Process: .09 seconds
- 4 Processes:   .07 seconds
"""

import argparse
from multiprocessing import Pool
from time import time
from utils import is_prime

def chunk_range(start, end, chunks):
    step = (end - start) // chunks
    ranges = [(start + i * step, start + (i + 1) * step) for i in range(chunks)]
    ranges[-1] = (ranges[-1][0], end)  # Ensure full coverage
    return ranges

def find_primes_in_range(rng):
    start, end = rng
    return [n for n in range(start, end) if is_prime(n)]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("start", type=int, help="Start of range (inclusive)")
    parser.add_argument("end", type=int, help="End of range (exclusive)")
    parser.add_argument("processes", type=int, help="Number of processes to use")
    args = parser.parse_args()

    ranges = chunk_range(args.start, args.end, args.processes)

    start_time = time()
    with Pool(processes=args.processes) as pool:
        results = pool.map(find_primes_in_range, ranges)
    all_primes = sorted([num for sublist in results for num in sublist])
    end_time = time()

    print(f"Primes found: {len(all_primes)}")
    print(f"Execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()