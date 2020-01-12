
def get_file_name():
    file_name = input("file:")
    return file_name


def read():
    file_name = get_file_name()

    with open(file_name) as text_file:
        p1 = [line.strip().split() for line in text_file]

    p1[0][0] = int(p1[0][0])

    for i in range(1, len(p1)):
        for j in range(0, 6):
            p1[i][j] = int(p1[i][j])

    return p1
