import time

def walk(chart, start):
    dir = -1j
    visited = set()
    visited.add(start)
    dir_vis = set()
    dir_vis.add((start, dir))
    while True:
        if start+dir not in chart: return 0, visited
        while chart[start+dir] == "#": dir *= 1j
        start += dir
        visited.add(start)
        if (start,dir) in dir_vis: return 1, visited
        dir_vis.add((start, dir))




with open("./2024/6/input.txt", "r") as f:
    d = [i.strip() for i in f.readlines()]


chart = dict()
for a in range(len(d)):
    for b in range(len(d[0])):
        chart[a*1j+b] = d[a][b]
        if d[a][b] == "^": start = a*1j+b

_, visited = walk(chart, start)
print(len(visited))
cnt = 0
t = time.time()
for i in visited:
    if chart[i] in ["#", "^"]: continue
    chart[i] = "#"
    loop, _ = walk(chart,start)
    chart[i] = "."
    cnt += loop

print(time.time()-t)
print(cnt)
