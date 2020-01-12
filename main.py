from classes.FCFS import *
from classes.SJF import *
from classes.PBS import *
from classes.RR import *
from classes.input import *

processes = []
n = 0


def return_n():
    nn = input("Number of processes: ")
    return int(nn)


def input_processes(n, p):
    count = 0

    while count < n:
        print("Process", count)
        at = input("Process arrival time: ")
        bt = input("Process burst time: ")
        while bt == 0:
            print("Error, burst time=0. Choose burst time greater than 0")
            bt = input("Process burst time: ")
        if p == 1:
            pp = input("Process priority: ")
            processes.append([int(count), int(bt), int(at), int(pp), 0, 0, 0])
        elif p == 0:
            processes.append([int(count), int(bt), int(at), 0, 0, 0, 0])

        count += 1

    return processes


b = input("Choose an algorithm"
          "\n1 - FCFS"
          "\n2 - SJF"
          "\n3 - Round-robin"
          "\n4 - Priority Based"
          "\nelse - exit"
          "\n")

if b != "1" and b != "2" and b != "3" and b != "4":
    exit(0)

a = input("1 - read processes from file"
          "\n2 - get processes from user"
          "\nelse - exit"
          "\n")

if a == "2":
    n = return_n()
    while n == 0:
        print("Error, n=0. Choose n greater than 0")
        n = return_n()
    if b == "1" or b == "3" or b == "2":
        processes = input_processes(n, 0)
    elif b == "4":
        processes = input_processes(n, 1)
elif a == "1":
    p1 = read()
    data = p1[0]
    processes = p1
    del processes[0]
    n = data[0]
else:
    exit(0)

if b == "1":
    fcfs = FCFS(processes, n)
    fcfs.find_avg(processes, n)
elif b == "2":
    sjf = SJF(processes, n)
    sjf.find_avg(processes, n)
elif b == "3":
    rr = RR(processes, n)
    rr.find_avg(processes, n)
elif b == "4":
    pbs = PBS(processes, n)
    pbs.find_avg(processes, n)
else:
    exit(0)
