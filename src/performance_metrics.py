from typing import Dict, List


def compute_waiting_time(processes: List[Dict], completion_times: Dict[int, float]) -> Dict[int, float]:
    waiting = {}
    for proc in processes:
        pid = proc['pid']
        waiting[pid] = completion_times[pid] - proc['arrival_time'] - proc['burst_time']
    return waiting


def compute_turnaround_time(processes: List[Dict], completion_times: Dict[int, float]) -> Dict[int, float]:
    turnaround = {}
    for proc in processes:
        pid = proc['pid']
        turnaround[pid] = completion_times[pid] - proc['arrival_time']
    return turnaround


def evaluate_schedule(processes: List[Dict], completion_times: Dict[int, float]) -> Dict[str, float]:
    waiting = compute_waiting_time(processes, completion_times)
    turnaround = compute_turnaround_time(processes, completion_times)
    avg_wait = sum(waiting.values()) / len(processes)
    avg_turn = sum(turnaround.values()) / len(processes)
    return {
        "average_waiting_time": avg_wait,
        "average_turnaround_time": avg_turn,
    }
