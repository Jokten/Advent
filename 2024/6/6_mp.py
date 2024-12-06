import time
import multiprocessing

def walk(chart, start, p):
    dir = -1j
    visited = set()
    if p == 1: visited.add(start)
    else: visited.add((start, dir))
    while True:
        if start+dir not in chart: return 0 if p == 2 else visited
        while chart[start+dir] == "#": dir *= 1j
        start += dir
        if p == 2 and (start,dir) in visited: return 1
        if p == 1: visited.add(start)
        else: visited.add((start, dir))

def mp2(chart, start, step, visited, q, id):
    cnt = 0
    for i in visited[id::step]:
        if chart[i] in ["#", "^"]: continue
        loop = walk(chart | {i: '#'},start,2)
        cnt += loop
    q.put(cnt)



with open("./2024/6/input.txt", "r") as f:
    d = [i.strip() for i in f.readlines()]


chart = dict()
for a in range(len(d)):
    for b in range(len(d[0])):
        chart[a*1j+b] = d[a][b]
        if d[a][b] == "^": start = a*1j+b

visited = walk(chart, start, 1)
print(len(visited))
visited = list(visited)

processes = []
q = multiprocessing.Queue()
cnt = 0
step = multiprocessing.cpu_count()
t = time.time()
for i in range(step):
    p = multiprocessing.Process(target=mp2, args=(chart,start,step,visited, q, i))
    processes.append(p)
    p.start()
for p in processes: p.join()


while not q.empty(): cnt+=q.get()

print(time.time()-t)
print(cnt)
