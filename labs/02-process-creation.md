# Lab 2: Process Creation and Management

## Goal

Students will understand process creation, child processes, and basic management operations.

## Tasks

1. Create a Python script that spawns child processes.
2. Observe the parent-child relationship using `ps`.
3. Explain the effects of `fork`, `exec`, and `wait` semantics.
4. Practice process termination and signal handling.

## Questions

- What happens when a parent process exits before its child?
- Why is process management important in multi-user systems?
- How does a shell use process creation to start programs?

## Example Python

```python
import os

pid = os.fork()
if pid == 0:
    print("child")
else:
    print("parent")
```

## Deliverable

Submit a brief explanation of the parent-child process relationship and the observed command output.
