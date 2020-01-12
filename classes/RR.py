from classes.display import *


class RR:
    def __init__(self, processes, n):
        self.processes = processes
        self.n = n

    def find_avg(self, processes, n):
        processes = sorted(processes, key=lambda x: x[2])
        g = []

        moment = 0 # aktualny moment działania algorytmu
        nn = n # zmienna określająca liczbę procesów do wykonania
        final_moment = 0

        q = input("Set time slice")
        q = int(q)

        n_q = 0  # indeks aktualnie przetwarzanego procesu
        queue = []

        while nn != 0:
            # procesy które już przyszły trafiają na kolejkę
            for i in range(0, n):
                if processes[i][2] <= moment and processes[i][3] == 0:
                    pid1 = processes[i][0]
                    bt1 = processes[i][1]
                    at1 = processes[i][2]
                    d1 = processes[i][3]
                    wt1 = processes[i][4]
                    tat1 = processes[i][5]
                    queue.append([pid1, bt1, at1, d1, wt1, tat1])
                    processes[i][3] = 2  # flaga że proces dodany do kolejki

            if n_q >= len(queue):
                n_q = 0

            if len(queue) > 0:
                if queue[n_q][1] > q:
                    queue[n_q][1] = queue[n_q][1] - q
                    moment = moment + q
                    for i in range(0,q):
                        g.append(queue[n_q][0])
                    n_q = n_q + 1
                    final_moment = final_moment + q

                elif queue[n_q][1] <= q:
                    moment = moment + queue[n_q][1]
                    final_moment = final_moment + queue[n_q][1]
                    for i in range(0,queue[n_q][1]):
                        g.append(queue[n_q][0])
                    for d in range(0, n):
                        if queue[n_q][0] == processes[d][0]:
                            processes[d][3] = 1
                            processes[d][5] = moment - processes[d][2]  # tat
                            processes[d][4] = processes[d][5] - processes[d][1]  # wt

                            nn = nn - 1

                    del queue[n_q]
            else:
                moment = moment + 1
                g.append("x")
                final_moment = final_moment + 1

        print(final_moment)
        display(processes, n, 0)
        gantt(g, final_moment)

        r = input("report? 1 for yes, 2 for no")
        while r != "1" and r != "2":
            r = input("Error, choose 1 for yes or 2 for no.")
        if r == "1":
            g1 = get_str_gantt(g, final_moment)
            raport(processes, n, 0, q, g1)
