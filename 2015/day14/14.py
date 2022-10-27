import numpy as np
import itertools
if __name__ == '__main__':
    with open('day14\input.txt') as file:
        data = file.read().splitlines()
    stat = []
    deers = {}
    for i in data:
        k = i.split()
        stat.append([k[0], int(k[3]), int(k[6]), int(k[-2])])
        deers[k[0]] = 0
    time = 2503
    max = 0

    for t in range(1,time+1):
        points = []
        for i in stat:
            dist = (t//(i[2]+i[3]))*(i[2]*i[1]) + min(((t%(i[2]+i[3])),i[2]))*i[1]
            points.append([i[0],dist])
        lead = sorted(points, key=lambda x: x[1])[-1][1]
        for i in list(filter(lambda x: x[1]==lead, points)):
            deers[i[0]] += 1
    
    print(deers)
    print(sum(deers.values()))
