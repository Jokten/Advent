from functools import cache
from time import perf_counter

def parser():
    with open(r'2022\14\input.txt', 'r') as openfile:
        data = openfile.read().splitlines()
    rocks = set()
    for row in data:
        r = []
        for cords in row.split(' -> '): r.append(tuple([int(i) for i in cords.split(',')]))
        for k in range(len(r)-1):
            upx = max([r[k][0], r[k+1][0]])
            downx = min([r[k][0], r[k+1][0]])
            upy = max([r[k][1], r[k+1][1]])
            downy = min([r[k][1], r[k+1][1]])
            for i in range(downx, upx+1):
                for j in range(downy, upy+1):
                    rocks.add((i, j))
    return rocks

@cache
def neighbours(cords):
    return [(cords[0], cords[1]+1), (cords[0]-1, cords[1]+1), (cords[0]+1, cords[1]+1)]
            
def main():
    occupied = parser()
    void = 1
    tot = 0
    part1= 0
    while void:
        cur = (500, 0)
        while True:
            ne = [i for i in neighbours(cur) if (i not in occupied) and i[1] < 171]
            if ne: cur = ne[0]
            else:
                occupied.add(cur)
                tot += 1
                break
            if cur[1] >= 169 and part1 == 0:
                print('Part 1: ',tot)
                part1 = 1
        if (500, 0) in occupied:
            void = 0
    print('Part 2: ',tot)


if __name__ == '__main__':
    start = perf_counter()
    main()
    print(f'Time: {perf_counter()-start}')