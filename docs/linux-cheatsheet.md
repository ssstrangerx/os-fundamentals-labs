# Linux Cheat Sheet

## Process Commands

```bash
ps -ef
ps aux --forest
top
htop
pstree
```

## Process Control

```bash
sleep 30 &
jobs
kill PID
kill -9 PID
nice -n 5 python script.py
```

## Scheduling Observations

```bash
ps -eo pid,ppid,comm,stat,%cpu,%mem --sort=-%cpu
```

## Thread Inspection

```bash
ps -L -p PID
top -H -p PID
```

## System Information

```bash
uname -a
cat /proc/cpuinfo
free -h
```

## IPC Notes

- Pipes connect related processes.
- Queues provide safe message passing between processes.
- Shared memory allows multiple processes to access common data.
- Synchronization is required when multiple processes or threads modify shared state.
