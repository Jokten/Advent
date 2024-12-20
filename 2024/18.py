import aoc, re
import time
import heapq
data = aoc.get_data(2024,18).split("\n")
t = time.time()
bytt  = [tuple(map(int, re.findall(r"\d+",i))) for i in data]
SIZE = 71
c = 1024
maxx = len(bytt)
bott = 1024
while True:
    byt = bytt[:c]
    mem = {(i,j): 99999 for i in range(SIZE) for j in range(SIZE) if (i,j) not in byt}
    mem[(0,0)] = 0
    pq, prev = [(0,(0,0))], {}
    byt = bytt[:c]        
    while(pq):
        s, cur = heapq.heappop(pq)
        for d in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            nex = cur[0] + d[0], cur[1] + d[1]
            if nex not in mem: continue
            if mem[nex] > s+1:
                mem[nex], prev[nex] = s+1, cur
                heapq.heappush(pq,(mem[nex], (nex)))
    if c==1024: print(mem[(SIZE-1,SIZE-1)])
    if mem[(SIZE-1,SIZE-1)] == 99999:
        if maxx-bott == 1: break
        else: maxx = c
    else: bott = c
    c = bott + max((maxx-bott)//2,1)
print(time.time()-t)
    
print(bytt[c-1], c)
