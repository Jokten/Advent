def splitdata(x):
    lis = [i.split() for i in x]
    out = []
    for i in lis:
        new = [i[0], int(i[1])]
        out.append(new)
    return out


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
    command = splitdata(data)
    depth = 0
    pos = 0
    aim = 0
    for i in command:
        if i[0] == 'forward':
            pos += i[1]
            depth += i[1]*aim
        elif i[0] == 'down':
            aim += i[1]
        else:
            aim -= i[1]
    print(depth)
    print(pos)
    print(depth*pos)