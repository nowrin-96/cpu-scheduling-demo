# FCFS Scheduling Algorithm

# Sample input (You can modify this list)
processes = [
    {"pid": "P1", "arrival": 0, "burst": 5},
    {"pid": "P2", "arrival": 1, "burst": 3},
    {"pid": "P3", "arrival": 2, "burst": 8},
    {"pid": "P4", "arrival": 3, "burst": 6},
]

# Sort by arrival time
processes.sort(key=lambda x: x["arrival"])

# Initialize times
current_time = 0
gantt_chart = []
total_waiting_time = 0
total_turnaround_time = 0

print("Process\tArrival\tBurst\tStart\tFinish\tWaiting\tTurnaround")
for p in processes:
    start_time = max(current_time, p["arrival"])
    finish_time = start_time + p["burst"]
    waiting_time = start_time - p["arrival"]
    turnaround_time = finish_time - p["arrival"]
    
    total_waiting_time += waiting_time
    total_turnaround_time += turnaround_time
    current_time = finish_time
    
    # Add to Gantt Chart
    gantt_chart.append((p["pid"], start_time, finish_time))
    
    # Output table
    print(f"{p['pid']}\t{p['arrival']}\t{p['burst']}\t{start_time}\t{finish_time}\t{waiting_time}\t{turnaround_time}")

# Averages
n = len(processes)
print(f"\nAverage Waiting Time: {total_waiting_time / n:.2f}")
print(f"Average Turnaround Time: {total_turnaround_time / n:.2f}")

# Gantt Chart Visualization
print("\nGantt Chart:")
for pid, start, end in gantt_chart:
    print(f"| {pid} ", end="")
print("|")

for pid, start, end in gantt_chart:
    print(f"{start:<4}", end="")
print(f"{gantt_chart[-1][2]}")  # End time of last process
