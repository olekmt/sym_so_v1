class SJF:
    def __init__(self, processes, n):
        self.processes = processes
        self.n = n

    # znajduje czas oczekiwania danych procesow
    def find_waiting_time(self, processes, n):
        service_time = [0]*n
        service_time[0] = 0
        processes[0][4] = 0

        for i in range(1, n):
            service_time[i] = (service_time[i-1] + processes[i-1][1])

            processes[i][4] = service_time[i] - processes[i][2]

        return processes

    # znajduje czasy przetwarzania dla procesow
    def find_turn_around_time(self, processes, n):

        for i in range(0, n):
            processes[i][5] = processes[i][1] + processes[i][4]

        return processes

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
                    queue.append([processes[i][0], processes[i][1], processes[i][2], processes[i][3], processes[i][4], processes[i][5]])

            queue = sorted(queue, key=lambda x: x[1])

            if len(queue) > 0:
                proc_done.append([queue[0][0], queue[0][1], queue[0][2], queue[0][3], queue[0][4], queue[0][5]])
                moment = moment + queue[0][1]

                pid = queue[0][0]
                for d in range(0,len(queue)):
                    if pid == processes[d][0]:
                        processes[d][3] = 1


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