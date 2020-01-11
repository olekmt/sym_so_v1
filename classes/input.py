
def get_file_name():
    file_name = input("podaj adres pliku")
    return file_name


def read():
    file_name = get_file_name()

    f = open(file_name, "r")
    if f.mode == "r":
        f1 = f.readlines()
    elif f.mode != "r":
        print("blad wczytywania pliku")
        return -1

    processes = [x.strip() for x in f1]

    return processes
