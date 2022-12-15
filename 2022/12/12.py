import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)).split('2022')[0])
import aoctools
import heapq
import re

def distance(cur, end):
    return abs(cur[0]-end[0]) + abs(cur[1]-end[1])
    
def neighbors(data, x, y):
    neighbors = []
    if x > 0 and (data[x,y]-data[x-1,y]) >= -1: neighbors.append((x-1,y))
    if x < len(data)-1 and (data[x,y]-data[x+1,y]) >= -1: neighbors.append((x+1,y))
    if y > 0 and (data[x,y]-data[x,y-1]) >= -1: neighbors.append((x,y-1))
    if y < len(data[0])-1 and (data[x,y]-data[x,y+1]) >= -1: neighbors.append((x,y+1))
    return neighbors

def astar(data, start, end):
    q = []
    if len(start) == 2:
        heapq.heappush(q, (distance(start, end), 0, start))
    else:
        for starti in start: heapq.heappush(q, (distance(starti, end), 0, starti))
    visited = set()
    while q:
        cost, cur = heapq.heappop(q)[1:]
        if cur in visited: continue
        if cur == end: return cost
        visited.add(cur)
        for n in neighbors(data, cur[0], cur[1]):
            if n not in visited:
                heapq.heappush(q, (distance(n, end)+cost+1, cost+1, n))
    return -1

def main():
    data = aoctools.data_loader(2022, 12, two_parts=False)
    alt_start = []
    for e,i in enumerate(data):
        if re.search(r'S',i): start = (e,i.index('S'))
        if re.search(r'a',i):
            for a in re.finditer(r'a',i): alt_start.append((e,a.start()))
        if re.search(r'E',i): end = (e,i.index('E'))
    data = np.array([[ord(i) - ord('a') for i in row] for row in data])
    data [start] = 0
    data [end] = ord('z') - ord('a')

    print(astar(data, start, end)) # part 1
    print(astar(data, alt_start, end)) # part 2

if __name__ == '__main__':
    main()