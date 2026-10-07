# Lab 1: Linux Processes and System Services

## Goal

Students will use Linux utilities to understand processes, states, and services.

## Tasks

1. Run `ps -ef` and identify the system services running on the machine.
2. Use `top` or `htop` to observe CPU and memory activity.
3. Explain the difference between a process and a service.
4. Identify parent-child relationships among processes.
5. Discuss how the kernel schedules processes and manages resources.

## Questions

- What is a process?
- What are common process states?
- How does the OS decide which process runs next?
- Why do system daemons remain active in the background?

## Example Commands

```bash
ps -ef
ps aux --forest
pstree
top
```

## Deliverable

Submit 1–2 screenshots and a brief explanation of the observed system state.
