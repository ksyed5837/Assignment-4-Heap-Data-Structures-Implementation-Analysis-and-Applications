import random, time, csv
from statistics import median
from typing import List, Callable
from heapsort import heapsort
from other_sorts import randomized_quicksort, mergesort, is_sorted
def gen_random(n): return [random.randint(0, 10**6) for _ in range(n)]
def gen_sorted(n): return list(range(n))
def gen_reverse(n): return list(range(n, 0, -1))
def gen_repeated(n, k=5): return [random.randint(0, k-1) for _ in range(n)]
def time_once(fn: Callable[[List[int]], List[int]], data: List[int]) -> float:
    start=time.perf_counter(); out=fn(list(data)); elapsed=time.perf_counter()-start
    assert is_sorted(out); return elapsed
def run_bench(sizes=(1000,3000,6000), trials=3, out_csv="sort_benchmarks.csv"):
    gens=[("random",gen_random),("sorted",gen_sorted),("reverse",gen_reverse),("repeated",gen_repeated)]
    algs=[("heapsort",heapsort),("quicksort",randomized_quicksort),("mergesort",mergesort)]
    rows=[]
    for n in sizes:
        for gname,gfun in gens:
            base=gfun(n)
            for aname,afun in algs:
                times=[time_once(afun, base) for _ in range(trials)]
                rows.append({"n":n,"distribution":gname,"algorithm":aname,
                             "median_time":median(times),"mean_time":sum(times)/len(times),
                             "trial_times":";".join(f"{t:.6f}" for t in times)})
                print(f"n={n:6d} {gname:8s} {aname:9s} median={median(times):.6f}s")
    with open(out_csv,"w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["n","distribution","algorithm","median_time","mean_time","trial_times"])
        w.writeheader(); w.writerows(rows)
if __name__=="__main__":
    run_bench()
