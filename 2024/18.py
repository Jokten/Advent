import aoc, re
import heapq
data = aoc.get_data(2024,18).split("\n")
bytt  = [tuple(map(int, re.findall(r"\d+",i))) for i in data]
SIZE = 71
c = 1024
maxx = len(bytt)

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
                heapq.heappush(pq,(s+1, (nex)))

    if (mem[(SIZE-1,SIZE-1)]) == 99999: break
    if c==1024: print(mem[(SIZE-1,SIZE-1)])
    p = [(SIZE-1,SIZE-1)]
    spots = set()
    while p:
        cur = p.pop()
        spots.add(cur)
        if cur in prev: p.append(prev[cur])
    
    while True:
        if bytt[c] in spots: break
        else: c+=1
    c += 1

print(bytt[c-1])
