def display(processes, n, p):

    total_wt = 0
    total_tat = 0

    if p == 0:
        print("Processes   Burst Time   Arrival Time     Waiting",
                "Time   Turn-Around Time  Completion Time \n")
    elif p == 1:
        print("Processes   Burst Time   Arrival Time  Priority   Waiting",
             "Time   Turn-Around Time  Completion Time \n")

    for i in range(0, n):
        total_wt = total_wt + processes[i][4]
        total_tat = total_tat + processes[i][5]

        compl_time = processes[i][5] + processes[i][2]

        if p == 0:
            print(" ", processes[i][0], "\t\t\t", processes[i][1], "\t\t\t", processes[i][2],
                 "\t\t\t\t", processes[i][4], "\t\t\t\t", processes[i][5], "\t\t\t\t ", compl_time)
        elif p == 1:
            print(" ", processes[i][0], "\t\t\t", processes[i][1], "\t\t\t", processes[i][2],
                    "\t\t\t\t", processes[i][3], "\t\t\t",  processes[i][4], "\t\t\t\t", processes[i][5],
                    "\t\t\t\t ", compl_time)

    print("Average waiting time = %.5f " % (total_wt / n))
    print("\nAverage turn around time = ", total_tat / n)

