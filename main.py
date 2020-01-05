from classes.FCFS import FCFS
from classes.SJF import SJF
from classes.HRRN import HRRN
from classes.RR import RR

processes = []
n = 0


def return_n():
    nn = input("Podaj liczbe procesow: ")
    return int(nn)


def input_processes_priority(n):  # TODO: klasa proces, medody input, return, upload from file
    count = 0

    while count < n:
        print("proces", count)
        at = input("Podaj czas przybycia procesu: ")
        bt = input("Podaj czas trwania procesu: ")
        p = input("Podaj priorytet")

        processes.append([int(count), int(bt), int(at), int(p), 0, 0])

        count += 1

    return processes


def input_processes(n):
    count = 0

    while count < n:
        print("proces", count)
        at = input("Podaj czas przybycia procesu: ")
        bt = input("Podaj czas trwania procesu: ")

        processes.append([int(count), int(bt), int(at), 0, 0, 0])

        count += 1

    return processes


b = input("Wybierz algorytm"
          "\n1 - FCFS"
          "\n2 - SJF"
          "\n3 - Round-robin"
          "\n4 - HRRN"
          "\ninne - wyjście"
          "\n")

a = input("wybierz pule procesow O- otwarta lub Z- zamknieta")


if a == 'O' or a == 'o':
    n = return_n()
    processes = input_processes(n)
elif a == 'Z' or a == 'z':
    exit(0)
else:
    exit(0)


if b == '1':
    fcfs = FCFS(processes, n)
    fcfs.find_avg(processes, n)
elif b == '2':
    sjf = SJF(processes, n)
    sjf.find_avg(processes, n)
elif b == '3':
    RR(processes, n)
elif b == '4':
    HRRN(processes, n)
else:
    exit(0)
