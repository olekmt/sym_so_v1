# klasa, do której naleza metody zwiazane z algorytmem, obliczaniem wartosci oraz wyswietlaniem
from classes.display import *

class FCFS:
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

    # znajduje srednie czasy oczekiwania i przetwarzania, wyswietla dane o procesach
    def find_avg(self, processes, n):
        processes = sorted(processes, key=lambda x: x[2])

        processes = self.find_waiting_time(processes, n)
        processes = self.find_turn_around_time(processes, n)

        display(processes, n, 0)

        r = input("report? 1 for yes, 2 for no")
        while r != '1' or r != '2':
            r = input("Error, choose 1 for yes or 2 for no.")
        if r == "1":
            raport(processes, n, 0, 0)
