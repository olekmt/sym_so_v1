from classes.display import *


class FCFS:

    def __init__(self, processes, n):
        self.processes = processes
        self.n = n

    def find_avg(self, processes, n):
        processes = sorted(processes, key=lambda x: x[2])
        proc_done = []
        g = []

        moment = 0
        nn = n

        while nn != 0:
            queue = []

            for i in range(0, n):
                if processes[i][2] <= moment and processes[i][3] == 0:
                    queue.append(processes[i])

            if len(queue) > 0:
                queue = sorted(queue, key=lambda x: x[2])

                wt = moment - queue[0][2]
                tat = wt + queue[0][1]

                proc_done.append([queue[0][0], queue[0][1], queue[0][2], queue[0][3], int(wt), int(tat)])

                for d in range(0, n):
                    if queue[0][0] == processes[d][0]:
                        processes[d][3] = 1

                for i in range(0, proc_done[-1][1]):
                    g.append(proc_done[-1][0])

                moment = moment + queue[0][1]
                nn = nn - 1
            else:
                moment = moment + 1
                g.append("x")

        display(proc_done, n, 0)
        gantt(g, proc_done[-1][2] + proc_done[-1][5])

        r = input("report? 1 for yes, 2 for no: ")
        while r != "1" and r != "2":
            r = input("Error, choose 1 for yes or 2 for no.")
        if r == "1":
            g1 = get_str_gantt(g, proc_done[-1][2] + proc_done[-1][5])
            raport(proc_done, n, 0, 0, g1)
