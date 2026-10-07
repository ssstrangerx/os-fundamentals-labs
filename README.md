# Operating Systems Fundamentals Lab Suite

This repository is designed for a lab assignment focused on operating-system services, process creation, process management, CPU scheduling, threads, and inter-process communication (IPC). It combines Linux command-line exercises, Python implementations, and simulation tools that help students understand how operating systems manage work and resources.

## Learning Goals

Students will:
- Observe Linux processes and system state from the command line.
- Understand process creation, lifecycle, and management.
- Simulate and compare major CPU scheduling algorithms.
- Measure waiting time, turnaround time, response time, and throughput.
- Explore threads and synchronization issues in shared-memory programs.
- Demonstrate communication between cooperating processes using IPC primitives.
- Relate theory to practical Linux and Python examples.

## Lab Topics

1. Linux process exploration and system services
2. Process creation and management in Unix/Linux
3. CPU scheduling algorithms: FCFS, SJF, Priority, RR
4. Threads and race conditions
5. Inter-process communication: pipes, queues, and shared coordination
6. Performance evaluation and reporting

## Repository Structure

```text
os-fundamentals-labs/
├── README.md
├── requirements.txt
├── Makefile
├── docs/
│   ├── lab-manual.md
│   ├── grading-rubric.md
│   └── linux-cheatsheet.md
├── labs/
│   ├── README.md
│   ├── 01-linux-processes.md
│   ├── 02-process-creation.md
│   ├── 03-cpu-scheduling.md
│   ├── 04-threads.md
│   └── 05-ipc.md
├── src/
│   ├── __init__.py
│   ├── process_observer.py
│   ├── scheduling_simulator.py
│   ├── thread_demo.py
│   ├── ipc_demo.py
│   └── performance_metrics.py
├── scripts/
│   └── run_all_demos.py
├── tests/
│   └── test_scheduling_metrics.py
└── .gitignore
```

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_all_demos.py
```

## Available Demos

- Process observer: shows live system process information.
- Scheduling simulator: compares FCFS, SJF, Priority, and Round Robin.
- Thread demo: demonstrates synchronization and race conditions.
- IPC demo: uses multiprocessing queues and pipes.
- Performance metrics: computes statistics from process run data.

## Suggested Lab Workflow

1. Read the lab manual and Linux cheat sheet.
2. Complete the process observation exercises in Linux.
3. Run the scheduling simulator and analyze metrics.
4. Implement thread synchronization examples.
5. Demonstrate IPC communication between processes.
6. Submit a report with screenshots, tables, and interpretations.

## Problem-Solving Focus

This assignment emphasizes understanding the relationship between OS theory and real Linux behavior. Students are expected to reason about:
- process states and scheduling decisions
- resource sharing and contention
- fairness and throughput trade-offs
- communication patterns across processes
- correctness under concurrency

## License

This project is released under the MIT License.

## Authoring Note

This repository was created as a complete starter package for a lab assignment and includes a full set of learning materials and runnable examples.
