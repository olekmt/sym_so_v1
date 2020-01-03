class FCFS:
    def __init__(self, processes, n):
        self.processes = processes
        self.n = n

    def find_waiting_time(self, processes, n):
        service_time = [0]*n
        service_time[0] = 0
        processes[0][4] = 0

        for i in range(1, n):
            service_time[i] = (service_time[i-1] + processes[i-1][1])

            processes[i][4] = service_time[i] - processes[i][2]

        return processes

    def find_turn_around_time(self, processes, n):

        for i in range(0, n):
            processes[i][5] = processes[i][1] + processes[i][4]

        return processes

    def find_avg(self, processes, n):
        processes = self.find_waiting_time(processes, n)
        processes = self.find_turn_around_time(processes, n)

        total_wt = 0
        total_tat = 0

        print("Processes   Burst Time   Arrival Time     Waiting",
              "Time   Turn-Around Time  Completion Time \n")

        for i in range(0, n):
            total_wt = total_wt + processes[i][4]
            total_tat = total_tat + processes[i][5]

            compl_time = processes[i][5] + processes[i][2]

            print(" ", processes[i][0], "\t\t\t", processes[i][1], "\t\t\t", processes[i][2],
                  "\t\t\t\t", processes[i][4], "\t\t\t\t", processes[i][5], "\t\t\t\t ", compl_time)

        print("Average waiting time = %.5f " % (total_wt / n))
        print("\nAverage turn around time = ", total_tat / n)
