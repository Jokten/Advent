import heapq
import itertools

def addx(map):
    new_map = map.copy()
    for n in range(0,4):
        for row in range(len(new_map)):
            new_map[row] = new_map[row] + [((x+n) % 9) + 1 for x in map[row]]

    for n in range(0,4):
        for row in range(len(map)):
            new_map.append([((x+n) % 9) + 1 for x in new_map[row]])
    return new_map


def main():
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
    oldmap = [[int(j) for j in i] for i in data]

    with open('facit.txt', 'r') as file:
        data = file.read().splitlines()
    oldmap2 = [[int(j) for j in i] for i in data]

    maps = addx(oldmap)
    print(oldmap2 == maps)
    print(len(oldmap[0]))
    #maps = oldmap
    paths = {}
    visited = set()
    maps[0][0] = 0

    for i in maps:
        for j in i:
            print(j,end='')
        print()

    for i, j in itertools.product(range(len(maps)),range(len(maps[0]))):
        paths[(i, j)] = 100000
    paths[(0, 0)] = 0
    ko = []
    current = (0, 0)
    ex = 0

    while True:
        y = current[0]
        x = current[1]
        neighbor = [(y+1, x), (y, x+1), (y-1, x), (y, x-1)]
        for i in neighbor:
            if i not in visited and i in paths:
                if paths[i] > (paths[current] + maps[y][x]):
                    paths[i] = (paths[current] + maps[y][x])
                    heapq.heappush(ko, (paths[i],i))
                if i == (len(maps)-1, len(maps)-1):
                    leng = paths[i] + maps[len(maps)-1][len(maps)-1]
                    print(maps[len(maps)-1][len(maps)-1])
                    print(maps[y][x])

        visited.add(current)
        current = heapq.heappop(ko)[1]
        try:
            while current in visited:
                current = heapq.heappop(ko)[1]
        except IndexError:
            break
    print(leng)



if __name__ == '__main__':
    main()
