import pandas as pd
import matplotlib.pyplot as plt


# Round Robin Scheduling Implementation
def round_robin(processes, burst_time, arrival_time, quantum):
    n = len(processes)
    rem_bt = burst_time[:]  # remaining burst times
    t = 0
    complete = [0] * n  # completion time
    gantt_chart = []

    # Ready queue simulation
    ready_queue = []
    visited = [False] * n

    while True:
        # Add newly arrived processes
        for i in range(n):
            if arrival_time[i] <= t and not visited[i]:
                ready_queue.append(i)
                visited[i] = True

        if not ready_queue and all(rem == 0 for rem in rem_bt):
            break

        if not ready_queue:  # CPU idle
            t += 1
            continue

        # Pick process from queue
        idx = ready_queue.pop(0)
        exec_time = min(quantum, rem_bt[idx])

        # Record Gantt chart
        gantt_chart.append((processes[idx], t, t + exec_time))

        # Update time
        t += exec_time
        rem_bt[idx] -= exec_time

        # Add new arrivals during execution
        for i in range(n):
            if arrival_time[i] <= t and not visited[i]:
                ready_queue.append(i)
                visited[i] = True

        # If process not finished, put it back
        if rem_bt[idx] > 0:
            ready_queue.append(idx)
        else:
            complete[idx] = t

    # Calculate Turnaround & Waiting Times
    turnaround = [complete[i] - arrival_time[i] for i in range(n)]
    waiting = [turnaround[i] - burst_time[i] for i in range(n)]

    # Create results table
    df = pd.DataFrame({
        "Process": processes,
        "Arrival Time": arrival_time,
        "Burst Time": burst_time,
        "Completion Time": complete,
        "Turnaround Time": turnaround,
        "Waiting Time": waiting
    })

    avg_tat = sum(turnaround) / n
    avg_wt = sum(waiting) / n

    return df, gantt_chart, avg_tat, avg_wt


# Example input
processes = ["P1", "P2", "P3", "P4"]
arrival_time = [0, 1, 2, 3]
burst_time = [5, 3, 1, 2]
quantum = 2

# Run Round Robin
df, gantt, avg_tat, avg_wt = round_robin(processes, burst_time, arrival_time, quantum)

# ---------------- Matplotlib Output ----------------
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# --- (1) Gantt Chart ---
for p, start, end in gantt:
    ax[0].barh(y=0, width=end - start, left=start, edgecolor='black', align='center')
    ax[0].text((start + end) / 2, 0, p, ha='center', va='center', color='white', fontsize=10)

ax[0].set_yticks([])
ax[0].set_xlabel("Time")
ax[0].set_title("Round Robin Scheduling - Gantt Chart")
ax[0].set_xlim(0, max(end for _, _, end in gantt) + 1)
ax[0].grid(axis="x", linestyle="--", alpha=0.6)

# --- (2) Table + Stats ---
# Convert DataFrame to matplotlib table
table_data = [df.columns.to_list()] + df.values.tolist()
table = ax[1].table(cellText=table_data, loc="center", cellLoc="center", colLabels=None)

# Style the table
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

ax[1].axis("off")
ax[1].set_title(f"Round Robin Scheduling Results\nAvg Turnaround Time = {avg_tat:.2f}, Avg Waiting Time = {avg_wt:.2f}",
                fontsize=12)

plt.tight_layout()
plt.show()
