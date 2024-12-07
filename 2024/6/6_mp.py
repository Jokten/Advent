import time

from multiprocessing import Queue, cpu_count, Process
def walk(chart, start):
    visited, dir = {(start,-1j)}, -1j
    while True:
        if start+dir not in chart: return {p[0] for p in visited}
        while chart[start+dir] == "#": dir *= 1j
        start += dir
        if (start,dir) in visited: return 1
        visited.add((start, dir))

def mp2(chart, start, step, visited, q, id):
    q.put(sum(1 == walk(chart | {i: '#'},start) for i in visited[id::step] ))

def main():
    t = time.time()
    d = [i.strip() for i in open("./2024/6/input.txt", "r").readlines()]

    chart = {a*1j+b:d[a][b] for a in range(len(d)) for b in range(len(d[0]))}
    start = [i[0] for i in chart.items() if i[1] == '^'][0]

    visited = list(walk(chart, start))

    processes, cnt, q, step = [], 0, Queue(), cpu_count()

    for i in range(step):
        p = Process(target=mp2, args=(chart,start,step,visited, q, i))
        processes.append(p)
        p.start()

    for p in processes: p.join()
    while not q.empty(): cnt+=q.get()
    print(f"Part 1: {len(visited)}\nPart 2: {cnt}\nTime: {time.time()-t:0.2f}s")
    

if __name__ == "__main__":
    main()