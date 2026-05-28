# 📚 Parallel Computing Study Resources & Guides

Welcome to the **Parallel and Distributed Computing Study Resources** directory! This folder houses high-yield, comprehensive study guides, course mapping files, and exam review notes for CS-440 (Parallel and Distributed Computing).

These documents serve as a critical academic resource, distilling complex multi-threaded architectural details, mutual exclusion mathematics, and distributed synchronization guidelines into easy-to-read, structured cheat-sheets.

---

## 📂 Study Resource Directory

This directory contains the following primary study files:

*   **🗺️ Course Topics & Skills Mapping**:
    *   [COURSE_TOPICS_MAPPING.md](./COURSE_TOPICS_MAPPING.md) — Comprehensive outline connecting course lectures, lab projects, standard textbook sections, and practical learning milestones.
*   **📝 Exam & Quiz High-Yield Review Sheets**:
    *   [PDC_QUIZ_STUDY_GUIDE.md](./PDC_QUIZ_STUDY_GUIDE.md) — Targeted review sheet covering threads, processes, Flynn's Taxonomy, memory architectures, and Amdahl's Law calculations.
    *   [PDC_QUIZ_COMPREHENSIVE_STUDY_GUIDE.md](./PDC_QUIZ_COMPREHENSIVE_STUDY_GUIDE.md) — Deep-dive study guide covering advanced synchronization primitives, memory barriers, OpenMP directives, MPI communication calls, cache coherence (MESI protocol), and distributed load-balancing algorithms.

---

## 🧠 Key Study Highlights

### 1. Synchronization Primitives & Thread Safety
*   **Mutexes vs. Semaphores**: Mutual exclusion locks (binary lockstates) vs. signaling channels (counting semaphores) managing resource limits.
*   **Condition Variables**: Allowing threads to suspend execution safely while waiting for boolean resource signals, preventing CPU-hogging polling loops.
*   **Deadlock Prevention**: Managing Coffman's four conditions (Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait) by enforcing static resource acquisition orderings.

### 2. Modern Parallel Extensions
*   **OpenMP (Shared Memory API)**: Utilizing simple compiler pragmas (e.g., `#pragma omp parallel for`) to automatically partition loop iterations across threads, schedule workloads (Static, Dynamic, Guided), and manage variable scopes (`shared` vs. `private`).
*   **MPI (Message Passing Interface)**: Coordinating distributed clusters using point-to-point communication (`MPI_Send`, `MPI_Recv`) and collective operations (`MPI_Bcast`, `MPI_Reduce`, `MPI_Scatter`, `MPI_Gather`).

### 3. Hardware Constraints & Cache Coherence
*   **False Sharing**: Occurs when multiple independent threads write to distinct variables residing on the same CPU cache line. This triggers continuous cache invalidation cycles (cache bouncing), heavily degrading performance.
*   **MESI Protocol**: The four states (Modified, Exclusive, Shared, Invalid) used to enforce cache coherence across multi-core systems.
