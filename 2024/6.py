import time

with open("input.txt", "r") as f:
    d = [i.strip() for i in f.readlines()]
chart = dict()
for a in range(len(d)):
    for b in range(len(d[0])):
        chart[a*1j+b] = d[a][b]
        if d[a][b] == "^": ostart = a*1j+b
dir = -1j
visited = set()
visited.add(ostart)
start = ostart
while True:
    if start+dir not in chart: break
    elif chart[start+dir] == "#": dir *= 1j
    else:
        start += dir
        visited.add(start)
print(len(visited))

cnt = 0
print(ostart)
t = time.time()
for i in visited:
    if chart[i] in ["#", "^"]: continue
    if i == ostart: continue
    chart[i] = "#"
    dir = -1j
    visited2 = set()
    visited2.add((ostart,dir))
    start = ostart
    while True:
        if start+dir not in chart: break
        if chart[start+dir] == "#":
            dir *= 1j
            visited2.add((start,dir))
        start += dir
        if (start, dir) in visited2:
            cnt +=1
            break
        
    chart[i] = "."
print(time.time()-t)
print(cnt)
