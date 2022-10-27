def check_value(diff):
    if diff < 0:
        return -1
    elif diff == 0:
        return 0
    else:
        return 1

def create_line(cords):

    diffx = cords[1][0] - cords[0][0]
    diffy = cords[1][1] - cords[0][1]

    dy = check_value(diffy)
    dx = check_value(diffx)

    line = [cords[0]]
    while line[-1] != cords[1]:
        new_x = line[-1][0] + dx
        new_y = line[-1][1] + dy
        line.append([new_x, new_y])
    return line


def main():
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
    line = [create_line(h)  for h in [[[int(k) for k in j.split(',')] for j in i.split(' -> ')] for i in data]]
    cross = {}
    for i in line:
        for j in i:
            cross.setdefault(str(j), 0)
            cross[str(j)] += 1

    summa = 0
    for i in cross.values():
        if i > 1:
            summa += 1
    print(summa)
if __name__ == '__main__':
    main()
