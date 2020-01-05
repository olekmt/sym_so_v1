class SJF:
    def __init__(self, processes, n):
        self.processes = processes
        self.n = n

    def find_avg(self, processes, n):
        processes = sorted(processes, key=lambda x: x[2])
        proc_done = []

        total_wt = 0
        total_tat = 0
        moment = 0

        for j in range(0, n):
            queue = []

            for i in range(0, n):
                if processes[i][2] <= moment and processes[i][3] == 0:
                    queue.append([processes[i][0], processes[i][1], processes[i][2], processes[i][3], processes[i][4],
                                  processes[i][5]])

            if len(queue) > 0:
                queue = sorted(queue, key=lambda x: x[1])

                wt = moment - queue[0][2]
                tat = wt + queue[0][1]

                proc_done.append([queue[0][0], queue[0][1], queue[0][2], queue[0][3], int(wt), int(tat)])

                for d in range(0, len(queue)):
                    if queue[0][0] == processes[d][0]:
                        processes[d][3] = 1

                moment = moment + queue[0][1]

        print("Processes   Burst Time   Arrival Time     Waiting",
              "Time   Turn-Around Time  Completion Time \n")

        for i in range(0, n):
            total_wt = total_wt + proc_done[i][4]
            total_tat = total_tat + proc_done[i][5]

            compl_time = proc_done[i][5] + proc_done[i][2]

            print(" ", proc_done[i][0], "\t\t\t", proc_done[i][1], "\t\t\t", proc_done[i][2],
                  "\t\t\t\t", proc_done[i][4], "\t\t\t\t", proc_done[i][5], "\t\t\t\t ", compl_time)

        print("Average waiting time = %.5f " % (total_wt / n))
        print("\nAverage turn around time = ", total_tat / n)
