
def get_dir(x):
    match x:
        case '|':
            return 1j, -1j
        case '-':
            return 1, -1
        case '7':
            return -1, 1j
        case 'J':
            return -1, -1j
        case 'L':
            return 1, -1j
        case 'F':
            return 1, 1j
        case '.':
            return 0, 0
    

def main():
    open_file = open(r".\2023\10\input.txt", "r")
    lines = open_file.readlines()
    pipes = {}
    for i in range(len(lines)):
        if 'S' in lines[i]:
            start = i*1j+lines[i].index('S')
            print(f'Start: {start}')
        for j in range(len(lines[i])):
            pipes[(i*1j+j)] = lines[i][j]
            
    dirs = [1, 1j, -1, -1j]
    max = 0
    for dir in dirs:
        curr = start + dir
        if int(curr.real) < 0 or int(curr.imag) < 0 or int(curr.real) >= len(lines[0]) or int(curr.imag) >= len(lines):
            continue
        curr_dir = dir
        loop = [curr]
        while pipes[curr] != 'S':
            node = pipes[curr]
            pipe = get_dir(node)
            if -1*curr_dir not in pipe:
                break
            curr_dir = pipe[0] if pipe[0] != -1*curr_dir else pipe[1]
            curr = curr + curr_dir
            loop.append(curr)
        if len(loop)//2 > max:
            max = len(loop)//2
            max_loop = loop
    print(f'Part 1: {max}')

    first = max_loop[0]
    last = max_loop[-2]
    if last == first + 2 or last == first - 2:
        rep = '-'
    elif last == first + 2j or last == first - 2j:
        rep = '|'
    elif last == first + 1 + 1j:
        rep = '7'
    elif last == first + 1 - 1j:
        rep = 'J'
    elif last == first - 1 + 1j:
        rep = 'F'
    elif last == first - 1 - 1j:
        rep = 'L'
    pipes[start] = rep
    filled = 0
    cops = (('F', 'J'), ('7', 'L'))
    max_set = set(max_loop)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if (i*1j+j) not in max_set:
                cc = 0
                cc = debugg(i*1j+j, lines, pipes, max_set)
                if cc == 4:
                    filled += 1
    print(f'Part 2: {filled}')


def debugg(point, lines, pipes, max_loop, deb=0):
    cc = 0
    cops = (('F', 'J'), ('7', 'L'))
    dirs = [1, 1j, -1, -1j]
    for dir in dirs:
        check = 0
        curr = point + dir
        while int(curr.real) >= 0 and int(curr.imag) >= 0 and int(curr.real) < len(lines[0]) and int(curr.imag) < len(lines):
            if curr in max_loop:
                if deb:print(curr, check)
                if (dir == 1j or dir == -1j):
                    if pipes[curr] == '-':
                        check += 1
                    else:
                        curpip = cops[0] if pipes[curr] in cops[0] else cops[1]
                        curr += dir
                        while curr in max_loop:
                            if pipes[curr] != '|':
                                check += pipes[curr] in curpip
                                break
                            curr += dir
                elif (dir == 1 or dir == -1):
                    if pipes[curr] == '|':
                        check += 1
                    else:
                        curpip = cops[0] if pipes[curr] in cops[0] else cops[1]
                        curr += dir
                        # if deb and dir == print('deb1',curr)

                        while curr in max_loop:
                            if pipes[curr] != '-':
                                check += pipes[curr] in curpip
                                break
                            curr += dir
            if deb and dir == 1:print(curr)
            
            curr += dir
        if check%2 == 1:
            cc += 1
    return cc


if __name__ == "__main__":
    main()
