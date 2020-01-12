from classes.display import *


class PBS:
    def __init__(self, processes, n):
        self.processes = processes
        self.n = n

    def find_avg(self, processes, n):
        processes = sorted(processes, key=lambda x: x[2])
        proc_done = []

        moment = 0
        nn = n

        while nn != 0:
            queue = []

            for i in range(0, n):
                if processes[i][2] <= moment and processes[i][6] == 0:
                    queue.append(processes[i])

            if len(queue) > 0:
                queue = sorted(queue, key=lambda x: x[3], reverse=True)

                for d in range(1, len(queue)):
                    if queue[0][3] == queue[d][3]:
                        if queue[0][2] > queue[d][2]:
                            queue[0], queue[d] = queue[d], queue[0]

                wt = moment - queue[0][2]
                tat = wt + queue[0][1]

                proc_done.append([queue[0][0], queue[0][1], queue[0][2], queue[0][3], int(wt), int(tat)])

                for d in range(0, n):
                    if queue[0][0] == processes[d][0]:
                        processes[d][6] = 1

                for d in range(0, n):
                    if processes[d][2] <= moment and processes[d][6] == 0:
                        processes[d][3] = processes[d][3] + 1

                moment = moment + queue[0][1]
                nn = nn - 1
            else:
                moment = moment + 1

        display(proc_done, n, 1)

        r = input("report? 1 for yes, 2 for no")
        while r != "1" or r != "2":
            r = input("Error, choose 1 for yes or 2 for no.")
        if r == "1":
            raport(processes, n, 1, 0)
