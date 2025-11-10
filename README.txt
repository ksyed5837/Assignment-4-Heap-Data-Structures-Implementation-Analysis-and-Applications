Assignment 4 — Heap Data Structures (Heapsort + Priority Queue)
Author: Kashif Ali Syed

----------------------------------------
Overview:
This project demonstrates two major heap-based implementations:
1. Heapsort — a comparison-based O(n log n) sorting algorithm.
2. Priority Queue — a max-heap structure for task scheduling.

----------------------------------------
How to Run:

1. Heapsort Demo
   Run:
   python heapsort.py
   → Displays a simple demonstration of heap-based sorting.

2. Performance Benchmarks
   Run:
   python benchmark_sorts.py
   → Compares Heapsort, Randomized Quicksort, and Mergesort.
   → Creates 'sort_benchmarks.csv' and 'heaps_benchmark_random.png'.

3. Priority Queue Demo
   Run:
   python priority_queue.py
   → Demonstrates insertion, extraction, and priority adjustment.

4. Scheduler Simulation
   Run:
   python scheduler_sim.py
   → Simulates task execution using a priority-based scheduler.

----------------------------------------
Summary of Findings:
- Heapsort consistently performs at O(n log n) for all data types.
- It is slightly slower than Quicksort on random data but more stable.
- Mergesort uses extra memory (O(n)) but guarantees O(n log n).
- The Priority Queue supports insert and extract operations in O(log n).
- Scheduler simulation confirms that higher-priority tasks are processed first.

----------------------------------------
Files:
- heapsort.py — Heapsort implementation
- other_sorts.py — Quicksort and Mergesort for comparison
- benchmark_sorts.py — Performance benchmark tool
- priority_queue.py — Binary Heap Priority Queue
- scheduler_sim.py — Simple priority-based scheduler
- sort_benchmarks.csv — Benchmark results
- heaps_benchmark_random.png — Performance chart
- Report.docx — Full report

----------------------------------------

