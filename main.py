from classes.FCFS import FCFS
from classes.SJF import SJF
from classes.PBS import PBS
from classes.RR import RR
from classes.display import Display

processes = []
n = 0


def return_n():
    nn = input("Podaj liczbe procesow: ")
    return int(nn)


def input_processes(n, p):
    count = 0

    while count < n:
        print("proces", count)
        at = input("Podaj czas przybycia procesu: ")
        bt = input("Podaj czas trwania procesu: ")
        if p == 1:
            pp = input("Podaj priorytet")
            processes.append([int(count), int(bt), int(at), int(pp), 0, 0, 0])
        elif p == 0:
            processes.append([int(count), int(bt), int(at), 0, 0, 0])

        count += 1

    return processes


b = input("Wybierz algorytm"
          "\n1 - FCFS"
          "\n2 - SJF"
          "\n3 - Round-robin"
          "\n4 - priorytetowy z postarzaniem"
          "\ninne - wyjście"
          "\n")

a = input("wybierz pule procesow O- otwarta lub Z- zamknieta")


if a == 'O' or a == 'o':
    n = return_n()
    if b == '1' or b == '2' or 'b' == 3:
        processes = input_processes(n, 0)
    elif b == '4':
        processes = input_processes(n, 1)
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
    rr = RR(processes, n)
    rr.find_avg(processes, n)
elif b == '4':
    pbs = PBS(processes, n)
    pbs.find_avg(processes, n)
else:
    exit(0)
