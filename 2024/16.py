import aoc
import heapq

def update(nex, cur, prev,chart,s, q):
    if nex not in chart: return
    if chart[nex] > s:
        chart[nex], prev[nex] = s, [cur]
        heapq.heappush(q,(s, nex[0], nex[1]))
    elif chart[nex] == s:
        prev[nex].append(cur)

data = aoc.get_data(2024,16).split("\n")
chart = {}
DIRS = ((0,1), (1,0), (-1,0), (0,-1))

for x, i in enumerate(data):
    for y, j in enumerate(i):
        if j != "#":
            for d in DIRS:
                chart[((x,y), d)] = 9999999999
        if j == "S": start = x,y
        if j == "E": end = x,y

q, prev = [], {}
chart[(start, (0,1))] = 0
prev[(start, (0,1))] = []

heapq.heappush(q,(0,start,(0, 1)))
while q:
    s, pos, d = heapq.heappop(q)
    update(((pos[0]+d[0], pos[1]+d[1]),d), (pos,d), prev, chart, s+1, q)
    update((pos,(d[1], d[0])), (pos,d), prev, chart, s+1000, q)
    update((pos,(-d[1], -d[0])), (pos,d), prev, chart, s+1000, q)

p, spots = [], set()
best = 9999999999
for i in DIRS:
    if chart[(end, i)] < best:
        p = [(end, i)]
        best = chart[(end, i)]

while p:
    cur = p.pop()
    spots.add(cur[0])
    for i in prev[cur]: p.append(i)
    
print(best, len(spots))
