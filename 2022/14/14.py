from functools import cache
from time import perf_counter

def parser():
    with open(r'2022\14\input.txt', 'r') as openfile:
        data = openfile.read().splitlines()
    rocks = set()
    dep = 0
    for row in data:
        r = []
        for cords in row.split(' -> '): r.append(tuple([int(i) for i in cords.split(',')]))
        for c1, c2 in zip(r,r[1:]):
            x = sorted([c1[0], c2[0]])
            y = sorted([c1[1], c2[1]])
            for i in range(x[0], x[1]+1):
                for j in range(y[0], y[1]+1):
                    rocks.add((i, j))
                    dep = max(dep, j)
    return rocks, dep

@cache
def neighbours(cords):
    return [(cords[0], cords[1]+1), (cords[0]-1, cords[1]+1), (cords[0]+1, cords[1]+1)]
            
def main():
    occupied, depth = parser()
    tot = 0
    part1= 0
    while (500, 0) not in occupied:
        cur = (500, 0)
        while True:
            ne = [i for i in neighbours(cur) if (i not in occupied) and i[1] < depth+2]
            if ne: cur = ne[0]
            else: break
            if cur[1] >= depth and part1 == 0:
                print('Part 1: ',tot)
                part1 = 1
        occupied.add(cur)
        tot += 1
    print('Part 2: ',tot)


if __name__ == '__main__':
    start = perf_counter()
    main()
    print(f'Time: {perf_counter()-start}')