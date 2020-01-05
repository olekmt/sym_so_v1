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

