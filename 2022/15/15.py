import re
import numpy as np
import time

def find_possible(y,dists):
    ran = []
    for i,j in dists.items():
        if abs(y-i[1]) <= j:
            diff = abs(y-i[1])-j
            ren = (i[0]+diff, i[0]-diff)
            ran.append(ren)
    ran.sort(key=lambda x: x[0])
    new= []
    cur=None
    for i in ran:
        if cur is None: cur = i
        elif cur[1]+1 >= i[0]: cur = (cur[0], max(i[1], cur[1]))
        else:
            new.append(cur)
            cur = i
    new.append(cur)
    return new

def main():
    parse_start = time.perf_counter()
    with open(r'2022\15\input.txt', 'r') as openfile:
        data = openfile.read().splitlines()
    data = [[int(j) for j in re.findall(r'-?\d+', i)] for i in data]
    dists = {}
    beacs = set()
    ref = 4000000
    y1 = 2000000
    dists = {(x, y): abs(x-a) + abs(y-b) for x, y, a, b in data}
    beacs = {(a, b) for x, y, a, b in data}
    parse_time = time.perf_counter() - parse_start
    # part 1
    ranges = find_possible(y1, dists)
    print(sum([i[1]-i[0]+1 for i in ranges])-sum([1 for i in dists.keys() if i[1] == y1]) - sum([1 for i in beacs if i[1] == y1]))

    # part 2

    for i in range(ref):
        ranges = find_possible(i, dists)
        red = [k for k in ranges if 0<k[1] and k[0]<ref]
        if len(red) > 1:
            print((red[0][1]+1),i)
            print((red[0][1]+1)*4000000+i)
            break
    
            
if __name__ == '__main__':
    sta = time.perf_counter()
    main()
    print(f'Time: {time.perf_counter()-sta}')