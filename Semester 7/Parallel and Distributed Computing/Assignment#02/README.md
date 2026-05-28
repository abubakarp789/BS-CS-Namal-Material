# 💻 Assignment #02: Parallel Algorithm Optimizations

Welcome to the **PDC Assignment #02** directory! This folder houses comprehensive codebase implementations, assignment sheets, and an optimized performance report focusing on **Advanced Parallel Algorithmic Paradigms** completed for CS-440 (Parallel and Distributed Computing).

The core of this assignment is a series of three highly intensive computational tasks written in Python, designed to evaluate the trade-offs of **multiprocessing synchronization**, **shared memory buffers**, and **dynamic task queues**.

---

## 📂 Directory Contents

*   **📄 Complete Assignment Deliverables**:
    *   [Abubakar_41_CS440_Assignment2.pdf](./Abubakar_41_CS440_Assignment2.pdf) — Abubakar's final submitted PDF report detailing algorithm pseudocodes, structural dependency charts, and detailed optimization analyses.
    *   [Advanced Parallel Algorithmic Paradigms.docx](./Advanced%20Parallel%20Algorithmic%20Paradigms.docx) — Editable source document of the parallel paradigms report.
    *   [Assignment 2.docx](./Assignment%202.docx) — Official question specification sheet.
*   **💻 Python Implementations (`Python Implementation/`)**:
    *   [task1_greedy.py](./Python%20Implementation/task1_greedy.py) — Greedy Bandwidth Allocation solver utilizing concurrent threads.
    *   [task2_dna.py](./Python%20Implementation/task2_dna.py) — DNA Sequence Alignment using zero-copy shared memory wavefront computations.
    *   [task3_timetabling.py](./Python%20Implementation/task3_timetabling.py) — Hard Constraint Satisfaction Problem (CSP) timetabling solver with a dynamic work queue.
    *   **[execution_results_optimized.md](./Python%20Implementation/execution_results_optimized.md)** — Comprehensive execution benchmark report detailing CPU timing and speedup gains.

---

## 🧠 Algorithms & Optimization Paradigms

This assignment implements three major computational algorithms, comparing their parallel vs. sequential execution times:

### 1. Greedy Bandwidth Allocation
*   **The Task**: Allocate a total bandwidth pool of size $B$ to millions of concurrent user requests based on high-yield priority factors.
*   **Parallel Pattern**: Task divided across a pool of concurrent worker threads.
*   **Critical Finding**: On a test run of **20,000,000 users**, sequential execution (5.12s) significantly outperformed parallel execution (15.63s). Due to Python's Global Interpreter Lock (GIL) and high object serialization (pickling) overheads, transferring massive dataset buffers to worker processes creates a severe bottleneck.

### 2. DNA Sequence Alignment (Wavefront DP)
*   **The Task**: Compute a massive $10,000 \times 10,000$ dynamic programming matrix to align genome structures using needle-in-a-haystack heuristics.
*   **Parallel Pattern**: Designed a **Zero-Copy Shared Memory** wavefront architecture using `multiprocessing.Array` and customized worker indexing locksteps.
*   **Critical Finding**: Yielded a massive performance boost (completed in **0.65s** vs. an estimated **150s+** sequentially). Utilizing shared memory buffers avoided pickling bottlenecks entirely, showcasing the raw performance capacity of multi-core CPUs.

### 3. Exam Timetabling (Hard CSP Solver)
*   **The Task**: Solve a complex scheduling schedule mapping $M$ exams to $S$ time slots while avoiding student exam clashes.
*   **Parallel Pattern**: Implemented a parallel backtracking solver utilizing a **Dynamic Work Queue** to distribute branch exploration.
*   **Critical Finding**: The solver efficiently splits the solution space into 56 distinct sub-branches, distributing them across 32 physical worker processes to balance load and prevent idle worker cores.

---

## 📈 Performance Summary (i9-14900K / 32GB RAM)

| Task | Configuration | Sequential Time | Parallel Time | Speedup Factor | Primary Bottleneck / Win |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Bandwidth Allocation** | 20M users, 32 Threads | 5.12s | 15.63s | **0.33x** | 🚫 Python object serialization (Pickling) overhead. |
| **DNA Alignment** | 10k x 10k matrix, 32 Workers | >150.00s | 0.65s | **~230.0x** | ⚡ Zero-Copy Shared Memory dynamic programming. |
| **Exam Timetabling** | 30 Exams, 8 Slots | ~0.00s | 0.23s | *N/A* | ⚙️ Heuristics resolved early; workload successfully balanced. |

---

## 🎓 Key Optimization Takeaways

1.  **Work-to-Overhead Ratio**: Parallelism only speeds up execution when individual thread work ($w$) is significantly larger than the synchronization/communication overhead ($c$). If $c \gg w$, adding threads actually degrades performance.
2.  **Shared Memory vs. Message Passing**: The DNA Alignment results show that shared memory buffers (avoiding data copying) are essential for parallelizing algorithms that process large datasets on single-node multi-core systems.
3.  **Dynamic vs. Static Scheduling**: Dynamic work queues prevent worker cores from idling, ensuring optimal load balancing when navigating highly unpredictable search trees (like backtracking CSP).
