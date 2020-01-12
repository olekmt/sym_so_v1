from classes.input import *


def display(processes, n, p):
    total_wt = 0
    total_tat = 0

    if p == 0:
        print("Processes   Burst Time   Arrival Time     Waiting",
              "Time   Turn-Around Time  Completion Time \n")
    elif p == 1:
        print("Processes   Burst Time   Arrival Time  Priority   Waiting",
              "Time   Turn-Around Time  Completion Time \n")

    for i in range(0, n):
        total_wt = total_wt + processes[i][4]
        total_tat = total_tat + processes[i][5]

        compl_time = processes[i][5] + processes[i][2]

        if p == 0:
            print(" ", processes[i][0], "\t\t\t", processes[i][1], "\t\t\t", processes[i][2],
                  "\t\t\t\t", processes[i][4], "\t\t\t\t", processes[i][5], "\t\t\t\t ", compl_time)
        elif p == 1:
            print(" ", processes[i][0], "\t\t\t", processes[i][1], "\t\t\t", processes[i][2],
                  "\t\t\t\t", processes[i][3], "\t\t\t", processes[i][4], "\t\t\t\t", processes[i][5],
                  "\t\t\t\t ", compl_time)

    print("Average waiting time = %.5f " % (total_wt / n))
    print("\nAverage turn around time = ", total_tat / n)


def raport(processes, n, p, q):
    file_name = get_file_name()

    total_wt = 0
    total_tat = 0

    with open(file_name, "w+") as text_file:
        if q != 0:
            str1 = "quantum time" + q + '\n'
            text_file.write(str1)

        if p == 0:
            text_file.write(
                "Processes   Burst Time   Arrival Time     Waiting Time   Turn-Around Time  Completion Time\n")
        elif p == 1:
            text_file.write(
                "Processes   Burst Time   Arrival Time  Priority   Waiting Time   Turn-Around Time  Completion Time\n")

        for i in range(0, n):
            total_wt = total_wt + processes[i][4]
            total_tat = total_tat + processes[i][5]

            compl_time = processes[i][5] + processes[i][2]

            if p == 0:
                str1 = " " + str(processes[i][0]) +"\t\t" + str(processes[i][1]) + "\t\t" + str(
                        processes[i][2]) + "\t\t" + str(processes[i][4]) + "\t\t" + str(
                        processes[i][5]) + "\t\t " + str(compl_time) + "\n"
            elif p == 1:
                str1 = " " + str(processes[i][0]) + "\t\t" + str(processes[i][1]) + "\t\t" + str(
                        processes[i][2]) + "\t\t" + str(processes[i][3]) + "\t\t" + str(
                        processes[i][4]) + "\t\t" + str(processes[i][5]) + "\t\t " + str(compl_time) + "\n"

            text_file.write(str1)

        text_file.write("Average waiting time = " + str((total_wt / n)))
        text_file.write("\nAverage turn around time = " + str((total_tat / n)))
