from classes.display import Display


class SJF:
    def __init__(self, processes, n):
        self.processes = processes
        self.n = n

    def find_avg(self, processes, n):
        processes = sorted(processes, key=lambda x: x[2])
        proc_done = []

        moment = 0
        nn = n

        while True:
            queue = []

            for i in range(0, n):
                if processes[i][2] <= moment and processes[i][3] == 0:
                    queue.append(processes[i])

            if len(queue) > 0:
                queue = sorted(queue, key=lambda x: x[1])

                wt = moment - queue[0][2]
                tat = wt + queue[0][1]

                proc_done.append([queue[0][0], queue[0][1], queue[0][2], queue[0][3], int(wt), int(tat)])

                for d in range(0, n):
                    if queue[0][0] == processes[d][0]:
                        processes[d][3] = 1

                moment = moment + queue[0][1]
                nn = nn - 1
            else:
                moment = moment + 1

            if nn == 0:
                break

        disp = Display(proc_done, n)
        disp.display(proc_done, n)
