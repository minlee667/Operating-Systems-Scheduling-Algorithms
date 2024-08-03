
nprocess = int(input("Enter the number of processes: "))
processes = []
at = []
bt = []

for i in range(nprocess):
    processes.append(i + 1)
    at.append(int(input(f"Enter arrival time for process {i + 1}: ")))
    bt.append(int(input(f"Enter burst time for process {i + 1}: ")))


process_info = list(zip(processes, at, bt))
process_info.sort(key=lambda x: x[1])
processes, at, bt = zip(*process_info)

ct = [0] * nprocess
tat = [0] * nprocess
wt = [0] * nprocess
gantt_chart = []

for i in range(nprocess):
    if i == 0:
        ct[i] = at[i] + bt[i]
        gantt_chart.append((f'P{processes[i]}', at[i], ct[i]))
    else:
        if at[i] > ct[i - 1]:
            gantt_chart.append(('Idle', ct[i - 1], at[i]))
            ct[i] = at[i] + bt[i]
        else:
            ct[i] = ct[i - 1] + bt[i]
        gantt_chart.append((f'P{processes[i]}', gantt_chart[-1][2], ct[i]))
        
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

print("Process\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
for i in range(nprocess):
    print(f"P{processes[i]}\t{at[i]}\t\t{bt[i]}\t\t{ct[i]}\t\t{tat[i]}\t\t{wt[i]}")

print("\nGantt Chart:")
for segment in gantt_chart:
    print(f"| {segment[0]} ", end="")
print("|")

for segment in gantt_chart:
    print(f"{segment[1]} ", end="")
print(f"{gantt_chart[-1][2]}")
