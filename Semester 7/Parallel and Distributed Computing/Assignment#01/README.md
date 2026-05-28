# 💻 Assignment #01: Parallel Execution & Scaling Theory

Welcome to the **PDC Assignment #01** directory! This folder archives the theoretical assignment completed for CS-440 (Parallel and Distributed Computing). 

The assignment focuses on the mathematical models that dictate the absolute limits of software parallelization, analyzing speedups, task structures, and hardware memory hierarchies.

---

## 📂 Directory Contents

*   **📄 Complete Assignment Deliverables**:
    *   [Abubakar_41_CS440_Assignment1.pdf](file:///c:/Users/abuba/OneDrive/Desktop/BS-CS-Namal-Material/Semester%207/Parallel%20and%20Distributed%20Computing/Assignment%2301/Abubakar_41_CS440_Assignment1.pdf) — Abubakar's final submitted PDF report containing full mathematical derivations, detailed diagrams, and step-by-step solutions.
    *   [Abubakar_41_CS440_Assignment1.docx](file:///c:/Users/abuba/OneDrive/Desktop/BS-CS-Namal-Material/Semester%207/Parallel%20and%20Distributed%20Computing/Assignment%2301/Abubakar_41_CS440_Assignment1.docx) — Editable source document of the submission.
    *   [Assignment 1.docx](file:///c:/Users/abuba/OneDrive/Desktop/BS-CS-Namal-Material/Semester%207/Parallel%20and%20Distributed%20Computing/Assignment%2301/Assignment%201.docx) — Official question sheet provided by the instructor.

---

## 🧠 Core Theoretical Concepts Solved

The assignment provides detailed analytical answers to the following foundational PDC topics:

### 1. Amdahl's Law vs. Gustafson's Law
*   **Amdahl's Law**: Evaluates the potential speedup of an application when execution size remains constant ($S_{latency}(s) = \frac{1}{(1-p) + \frac{p}{s}}$). It demonstrates that the serial fraction ($1-p$), representing code that cannot be parallelized, places a strict limit on maximum speedup, regardless of the number of processors added.
*   **Gustafson's Law**: Evaluates speedup from a scaled perspective, where problem size grows in proportion to the number of processor cores ($S_{scaling}(s) = s + (1-s)p$). It shows that large parallel systems can achieve high efficiency when data size is scaled dynamically.

```text
    Amdahl's Law (Fixed Workload)          Gustafson's Law (Scaled Workload)
    
     Processor 1:  [  Serial  ][  Parallel  ]         Processor 1:  [  Serial  ][  Parallel  ]
     Processor 4:  [  Serial  ][ P ][ P ][ P ]        Processor 4:  [  Serial  ][  P  ][  P  ][  P  ]
                   └──────────┬──────────────┘                      └──────────────┬────────────────┘
                        Fixed Workload                                      Scaled Workload
                (Serial bottleneck dominates)                           (High parallel scaling)
```

### 2. Flynn's Classical Taxonomy
*   A classification framework for computer architectures based on instruction and data streams:
    *   **SISD (Single Instruction, Single Data)**: Classic uniprocessor architectures (von Neumann).
    *   **SIMD (Single Instruction, Multiple Data)**: Vector processors, modern GPUs processing a single operation on large grids of data.
    *   **MISD (Multiple Instruction, Single Data)**: Rare, fault-tolerant systems (e.g., flight computers).
    *   **MIMD (Multiple Instruction, Multiple Data)**: Modern multi-core CPUs and distributed compute networks.

### 3. Memory Architectures: UMA vs. NUMA
*   **UMA (Uniform Memory Access)**: Shared memory model where all processors access system RAM with identical latency.
*   **NUMA (Non-Uniform Memory Access)**: Distributed shared memory model where memory access latency depends on the physical location of the memory relative to the processor core, necessitating NUMA-aware scheduling.
