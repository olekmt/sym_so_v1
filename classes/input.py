
def get_file_name():
    file_name = input("podaj adres pliku")
    return file_name


def read():
    file_name = get_file_name()

    with open(file_name) as text_file:
        p = [line.strip().split() for line in text_file]

    p[0][0] = int(p[0][0])

    for i in range(1, len(p)):
        for j in range(0, 6):
            p[i][j] = int(p[i][j])

    return p
