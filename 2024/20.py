import aoc
import heapq
import time

def run(mem,start):
    q, prev = [(0, start)], {}
    chart[(start)] = 0
    prev[(start)] = []
    while q:
        s, cur= heapq.heappop(q)
        if cur == end: return mem, prev
        for d in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            nex = cur[0] + d[0], cur[1] + d[1]
            if nex not in mem: continue
            if mem[nex] > s+1:
                mem[nex], prev[nex] = s+1, cur
                heapq.heappush(q,(mem[nex], (nex)))
    
data = aoc.get_data(2024,20).split("\n")
chart = {}
t = time.time()
for x, i in enumerate(data):
    for y, j in enumerate(i):
        if j != "#":
            chart[(x,y)] = 9999999999
        if j == "S": start = x,y
        if j == "E": end = x,y

mem, prevs = run(chart, start)
path = set()
p = [end]
pathl= []
while(p):
    c = p.pop()
    path.add(c)
    pre = prevs[c]
    if pre: p.append(pre)

offsets = []
for x in range(-20,21):
    ax = abs(x)
    for y in range(-20+ax, 21-ax):
        if ax+abs(y) < 2: continue
        offsets.append((x,y,ax+abs(y)))

res, res2 = 0, 0
for st in path:
    mst = mem[st]
    for x,y,dist in offsets:
        nex = mem.get((st[0]+ x, st[1] + y))
        if nex: 
            if nex - mst -  dist>= 100:
                if dist == 2: res += 1
                res2 += 1
                    
print(res2, res)
print(time.time()-t)
