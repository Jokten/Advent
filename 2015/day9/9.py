import numpy as np
if __name__ == '__main__':
    with open('day9\input.txt') as file:
        f = file.read().splitlines()
    data = [i[0].split(' to ')+[int(i[1])] for i in [k.split(' = ') for k in f]]
    data += [[i[1], i[0], i[2]] for i in data]

    def sale(visited, roads, current):
        if len(visited) == 8:
            return 0
        return max([i[2] + sale(visited.copy()+[i[1]], roads, i[1]) for i in filter(lambda x: x[1] not in visited and x[0] == current, roads)])
    
    cities = set()
    for i in data:
        cities.add(i[0])
    print(max([sale([j],data,j) for j in cities]))
    