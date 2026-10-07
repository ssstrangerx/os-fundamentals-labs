import os
import sys
from typing import List, Dict

try:
    import psutil
except ImportError:  # pragma: no cover
    psutil = None


def get_processes(limit: int = 15) -> List[Dict[str, object]]:
    """Return a list of top processes with their key metadata."""
    if psutil is None:
        raise RuntimeError("psutil is required. Install dependencies from requirements.txt.")

    rows = []
    for proc in psutil.process_iter(['pid', 'name', 'ppid', 'status', 'cpu_percent', 'memory_percent']):
        try:
            info = proc.info
            rows.append({
                'pid': info.get('pid', 0),
                'ppid': info.get('ppid', 0),
                'name': info.get('name', 'unknown'),
                'status': info.get('status', 'unknown'),
                'cpu_percent': round(float(info.get('cpu_percent', 0.0)), 2),
                'memory_percent': round(float(info.get('memory_percent', 0.0)), 2),
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    rows.sort(key=lambda item: (item['cpu_percent'], item['memory_percent']), reverse=True)
    return rows[:limit]


def display_process_table(limit: int = 15) -> None:
    processes = get_processes(limit)
    headers = ["PID", "PPID", "NAME", "STATE", "CPU%", "MEM%"]
    rows = [
        [
            str(p['pid']),
            str(p['ppid']),
            str(p['name']),
            str(p['status']),
            f"{p['cpu_percent']:.2f}",
            f"{p['memory_percent']:.2f}",
        ]
        for p in processes
    ]

    widths = [len(h) for h in headers]
    for row in rows:
        for idx, cell in enumerate(row):
            widths[idx] = max(widths[idx], len(cell))

    def fmt_line(items):
        return "  ".join(str(value).ljust(widths[i]) for i, value in enumerate(items))

    print(fmt_line(headers))
    print("-" * len(fmt_line(headers)))
    for row in rows:
        print(fmt_line(row))


def show_system_context() -> None:
    """Display basic Linux process and system context."""
    print("Current process:")
    print(f"- PID: {os.getpid()}")
    print(f"- Parent PID: {os.getppid()}")
    print(f"- User: {os.environ.get('USER', 'unknown')}")
    print("\nTop processes:")
    display_process_table(limit=10)


if __name__ == "__main__":
    show_system_context()
