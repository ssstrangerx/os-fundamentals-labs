from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class Process:
    pid: int
    name: str
    arrival_time: float
    burst_time: float
    priority: int = 0


@dataclass
class ScheduleResult:
    order: List[str]
    metrics: Dict[str, float]
    timeline: List[str]


def calculate_metrics(processes: List[Process], completion_times: Dict[int, float]) -> Dict[str, float]:
    waiting = {}
    turnaround = {}
    response = {}

    for p in processes:
        turnaround[p.pid] = completion_times[p.pid] - p.arrival_time
        waiting[p.pid] = turnaround[p.pid] - p.burst_time
        response[p.pid] = max(0.0, waiting[p.pid])

    avg_wait = sum(waiting.values()) / len(processes)
    avg_turnaround = sum(turnaround.values()) / len(processes)
    avg_response = sum(response.values()) / len(processes)
    total_burst = sum(p.burst_time for p in processes)
    throughput = len(processes) / max(total_burst, 1e-9)

    return {
        "average_waiting_time": avg_wait,
        "average_turnaround_time": avg_turnaround,
        "average_response_time": avg_response,
        "throughput": throughput,
        "waiting_times": waiting,
        "turnaround_times": turnaround,
        "response_times": response,
    }


def fcfs(processes: List[Process]) -> ScheduleResult:
    ordered = sorted(processes, key=lambda p: (p.arrival_time, p.pid))
    current_time = 0.0
    completion = {}
    timeline = []
    sequence = []

    for p in ordered:
        if current_time < p.arrival_time:
            current_time = p.arrival_time
        start = current_time
        end = current_time + p.burst_time
        completion[p.pid] = end
        current_time = end
        sequence.append(f"P{p.pid}")
        timeline.append(f"P{p.pid}: {start:.1f}-{end:.1f}")

    metrics = calculate_metrics(processes, completion)
    return ScheduleResult(order=sequence, metrics=metrics, timeline=timeline)


def sjf(processes: List[Process]) -> ScheduleResult:
    ready = []
    time = 0.0
    remaining = {p.pid: p.burst_time for p in processes}
    completion = {}
    sequence = []
    timeline = []

    pending = sorted(processes, key=lambda p: p.arrival_time)
    while pending or ready:
        while pending and pending[0].arrival_time <= time:
            ready.append(pending.pop(0))
        if not ready:
            time = pending[0].arrival_time
            continue

        ready.sort(key=lambda p: (p.burst_time, p.arrival_time, p.pid))
        current = ready.pop(0)
        start = time
        end = time + current.burst_time
        completion[current.pid] = end
        time = end
        sequence.append(f"P{current.pid}")
        timeline.append(f"P{current.pid}: {start:.1f}-{end:.1f}")

        while pending and pending[0].arrival_time <= time:
            ready.append(pending.pop(0))

    metrics = calculate_metrics(processes, completion)
    return ScheduleResult(order=sequence, metrics=metrics, timeline=timeline)


def priority(processes: List[Process], preemptive: bool = False) -> ScheduleResult:
    ordered = sorted(processes, key=lambda p: (p.arrival_time, p.priority, p.pid))
    time = 0.0
    ready = []
    completion = {}
    sequence = []
    timeline = []
    remaining = {p.pid: p.burst_time for p in processes}

    while ordered or ready:
        while ordered and ordered[0].arrival_time <= time:
            ready.append(ordered.pop(0))

        if not ready:
            time = ordered[0].arrival_time
            continue

        if preemptive:
            ready.sort(key=lambda p: (p.priority, p.arrival_time, p.pid))
            current = ready.pop(0)
        else:
            ready.sort(key=lambda p: (p.priority, p.arrival_time, p.pid))
            current = ready.pop(0)

        start = time
        end = time + remaining[current.pid]
        completion[current.pid] = end
        time = end
        sequence.append(f"P{current.pid}")
        timeline.append(f"P{current.pid}: {start:.1f}-{end:.1f}")
        remaining[current.pid] = 0

        while ordered and ordered[0].arrival_time <= time:
            ready.append(ordered.pop(0))

    metrics = calculate_metrics(processes, completion)
    return ScheduleResult(order=sequence, metrics=metrics, timeline=timeline)


def round_robin(processes: List[Process], quantum: float = 2.0) -> ScheduleResult:
    queue = []
    remaining = {p.pid: p.burst_time for p in processes}
    current_time = 0.0
    completion = {}
    sequence = []
    timeline = []
    pending = sorted(processes, key=lambda p: (p.arrival_time, p.pid))

    while pending or queue:
        while pending and pending[0].arrival_time <= current_time:
            queue.append(pending.pop(0))

        if not queue:
            current_time = pending[0].arrival_time
            continue

        current = queue.pop(0)
        run_time = min(quantum, remaining[current.pid])
        start = current_time
        end = current_time + run_time
        current_time = end
        remaining[current.pid] -= run_time
        sequence.append(f"P{current.pid}")
        timeline.append(f"P{current.pid}: {start:.1f}-{end:.1f}")

        while pending and pending[0].arrival_time <= current_time:
            queue.append(pending.pop(0))

        if remaining[current.pid] > 0:
            queue.append(current)
        else:
            completion[current.pid] = end

    metrics = calculate_metrics(processes, completion)
    return ScheduleResult(order=sequence, metrics=metrics, timeline=timeline)


def demo_scheduling() -> None:
    sample = [
        Process(1, "P1", 0, 5, 2),
        Process(2, "P2", 1, 3, 1),
        Process(3, "P3", 2, 6, 4),
        Process(4, "P4", 3, 2, 3),
    ]

    algorithms = {
        "FCFS": fcfs(sample),
        "SJF": sjf(sample),
        "Priority": priority(sample),
        "Round Robin (Q=2)": round_robin(sample, quantum=2),
    }

    for name, result in algorithms.items():
        print(f"\n{name}")
        print("Order:", " -> ".join(result.order))
        print("Timeline:", " ; ".join(result.timeline))
        print("Average Waiting:", round(result.metrics['average_waiting_time'], 2))
        print("Average Turnaround:", round(result.metrics['average_turnaround_time'], 2))
        print("Average Response:", round(result.metrics['average_response_time'], 2))


if __name__ == "__main__":
    demo_scheduling()
