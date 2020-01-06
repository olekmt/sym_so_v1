from classes.display import Display

class RR:
    def __init__(self, processes, n):
        self.processes = processes
        self.n = n


    def find_avg(self, processes, n):
        processes = sorted(processes, key=lambda x: x[2])

        moment = 0
        nn = n

        q = input("Podaj kwant czasu q")
        q = int(q)

        n_q = 0  # iterator aktualnie przetwarzanego procesu
        queue = []

        while nn != 0:
            # procesy które już przyszły trafiają na kolejkę
            for i in range(0, n):
                if processes[i][2] <= moment and processes[i][3] == 0:
                    queue.append(processes[i])
                    processes[i][3] == 2 #flaga że proces dodany do kolejki

            if n_q > len(queue):
                n_q = 0

            if len(queue) > 0:
                if queue[n_q][1] > q:
                    queue[n_q][1] = queue[n_q][1] - q
                    moment = moment + q
                elif queue[n_q][1] <= q:
                    moment = moment + queue[n_q][1]
                    for d in range(0, n):
                        if queue[n_q][0] == processes[d][0]:
                            processes[d][3] = 1
                            processes[d][5] = moment - processes[d][2]  # tat
                            processes[d][4] = processes[d][5] - processes[d][1]  # wt

                            nn = nn - 1

                    del queue[n_q]
            else:
                moment = moment + 1

            n_q = n_q + 1

        disp = Display(processes, n)
        disp.display(processes, n)
