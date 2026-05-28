# 💻 Parallel and Distributed Computing (CS-440)

Welcome to the **Parallel and Distributed Computing (PDC)** course directory! This folder houses comprehensive lecture slides, standard textbooks, study guides, assignment sheets, code implementations, and containerized load-balancing tasks completed during Semester 7.

This course teaches how to build high-throughput, low-latency applications by harnessing parallel processing units (multi-core CPUs, GPUs) and distributed networks (containerized clusters, load balancers), utilizing Amdahl's Law and Gustafson's Law to optimize performance.

---

## 📂 Directory Contents

This directory contains the following academic resources and subprojects:

*   **📘 Curriculum Details**:
    *   [PDC Course Outline.pdf](./PDC_Course_Outline.pdf) — Formal syllabus mapping credits, textbook chapters, and assessment parameters.
*   **📚 Core Textbooks & Overviews**:
    *   [An Introduction to Parallel Programming.pdf](./An%20Introduction%20to%20Parallel%20Programming.pdf) — Core reference text by Peter S. Pacheco.
    *   [Distributed Systems (3rd Ed).pdf](./mvsteen-distributed-systems-3rd-preliminary-version-3-01pre-2017-170215.pdf) — Comprehensive guide on distributed systems by Maarten van Steen and Andrew S. Tanenbaum.
    *   [Python Parallel & Concurrent Programming Overview.pdf](./Python%20Parallel%20%26%20Concurrent%20Programming%20Overview.pdf) — Guide on Python multi-threading, multi-processing, and asyncio.
*   **📑 Lecture Slides (LEC 1 to 13)**:
    *   Lectures delivered by **Dr. Muzamil Ahmed**, introducing parallel architectures, memory models (Shared vs. Distributed), MPI (Message Passing Interface), OpenMP, mutual exclusion, thread safety, and load balancing algorithms.
*   **🔧 Subdirectories**:
 
| Folder | Focus | Key Topics & Contents | Documentation |
| :--- | :---: | :--- | :---: |
| **[Assignment #01](./Assignment%2301/)** | Theoretical Foundations | Speedups, efficiency calculations, Amdahl's Law, Gustafson's Law, and Flynn's Taxonomy. | [Explore](./Assignment%2301/README.md) |
| **[Assignment #02](./Assignment%2302/)** | Algorithmic Paradigms | Greedy task scheduling, DNA Sequence Alignment, and Exam Timetabling optimization in Python. | [Explore](./Assignment%2302/README.md) |
| **[Project Details](./Project%20Details/)** | Study Guides & Maps | Comprehensive PDC exam mappings and high-yield review sheets for quizzes. | [Explore](./Project%20Details/README.md) |
| **[Task (Scaling Lab)](./Task/)** | Horizontal Scaling | Custom container scaling utilizing **Docker**, **Docker Compose**, and **Nginx Reverse Proxy**. | [Read README](./Task/README.md) |omputing/Task/README.md) |

---

## 🌟 Featured Project: Multi-User Remote Access System

The flagship development project for this course is the **Multi-User Remote Access System**:

> [!TIP]
> This system is designed as a high-throughput, concurrent client-server framework enabling remote command execution and access coordination across multiple concurrent users over TCP/UDP channels.

*   🔗 **[Multi-User Remote Access System Repository](https://github.com/abubakarp789/Multi-User-Remote-Access-System)** — Full source code, protocol designs, thread synchronization mechanisms, and multi-user scaling test sheets.

---

## 🐳 Featured Implementation: Docker Scaling & Load Balancing

A major highlight of this course was the design and implementation of a dynamic horizontally-scalable computation web app:

```text
                     Incoming HTTP Traffic
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Nginx Load Balancer │
                    │    (Port 8080)      │
                    └──────────┬──────────┘
                               │
         ┌─────────────────────┼─────────────────────┐
         ▼                     ▼                     ▼
 ┌───────────────┐     ┌───────────────┐     ┌───────────────┐
 │ App Container │     │ App Container │     │ App Container │
 │  Instance 1   │     │  Instance 2   │     │  Instance N   │
 └───────────────┘     └───────────────┘     └───────────────┘
```

### Highlights:
1.  **Nginx Load Balancing**: Configured with a Round-Robin algorithm to distribute concurrent computations across a fleet of Python Flask instances.
2.  **Concurrency Testing**: Developed testing harness `test_scaling.py` calculating the exact speedup metrics under varying scales (1 to N instances).
3.  **Amdahl's Law Evaluation**: Demonstrated how synchronization overheads (serial execution bottlenecks) cap overall system speedup.

Check the details directly in:
➡️ **[Docker Scaling Task README](./Task/README.md)**

---

## 🎓 Core Competencies Achieved

*   **Flynn's Classification**: Clear understanding of SISD, SIMD, MISD, and MIMD systems.
*   **Performance Metrics**: Mastering speedup calculations, efficiency ratios, cost factors, and execution scaling.
*   **Thread & Process Coordination**: Addressing race conditions, deadlocks, and designing thread-safe queues.
*   **Microservices Architecture**: Packaging python environments using multi-stage `Dockerfiles` and coordinating networks using `docker-compose.yml`.
