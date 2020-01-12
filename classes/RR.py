from classes.display import *


class RR:
    def __init__(self, processes, n):
        self.processes = processes
        self.n = n

    def find_avg(self, processes, n):
        processes = sorted(processes, key=lambda x: x[2])

        moment = 0 # aktualny moment działania algorytmu
        nn = n # zmienna określająca liczbę procesów do wykonania

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
                    n_q = n_q + 1
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

        display(processes, n, 0)

        r = input("report? 1 for yes, 2 for no")
        while r != '1' or r != '2':
            r = input("Error, choose 1 for yes or 2 for no.")
        if r == "1":
            raport(processes, n, 0, q)
