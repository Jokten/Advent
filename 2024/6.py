import aoc
def walk(chart, start):
    visited, dir = {(start,-1j)}, -1j
    while True:
        if start+dir not in chart: return {p[0] for p in visited}
        while chart[start+dir] == "#": dir *= 1j
        start += dir
        if (start,dir) in visited: return 1
        visited.add((start, dir))

def main():
    d = [i.strip() for i in aoc.get_data(2024,6).split("\n")]
    chart = {a*1j+b:d[a][b] for a in range(len(d)) for b in range(len(d[0]))}
    start = [i[0] for i in chart.items() if i[1] == '^'][0]
    visited = list(walk(chart, start))
    print(f"Part 1: {len(visited)}\nPart 2: {sum([1 == walk(chart|{i: "#"},start) for i in visited])}")
    
if __name__ == "__main__":
    main()