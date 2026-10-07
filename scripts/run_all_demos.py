#!/usr/bin/env python3

from src.process_observer import show_system_context
from src.scheduling_simulator import demo_scheduling
from src.thread_demo import run_thread_demo
from src.ipc_demo import run_ipc_demo


def main():
    print("=== Operating Systems Lab Demo Runner ===\n")
    print("1. Linux process observation")
    show_system_context()
    print("\n2. CPU scheduling comparison")
    demo_scheduling()
    print("\n3. Thread synchronization demo")
    run_thread_demo()
    print("\n4. IPC demo")
    run_ipc_demo()


if __name__ == "__main__":
    main()
