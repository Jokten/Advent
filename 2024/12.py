import aoc
from collections import defaultdict

data = aoc.get_data(2024,12).split("\n")
grid = defaultdict(lambda: 0)
for a in range(len(data)): 
    for b in range(len(data[0])):
        grid[a+1j*b] = data[a][b]

visited = set()
tot, tot2 = 0, 0
for i in list(grid.keys()):
    if i in visited: continue
    area, sides = 0, 0
    vis2 = set()
    q = [i]
    ctype = grid[i]
    while q:
        current = q.pop()
        if current in visited: continue
        visited.add(current)
        for dir in [1, -1j, 1j, -1]:
            neighbour = current + dir
            if grid[neighbour] != ctype:
                if (dir, neighbour) in vis2: continue
                sides += 1
                for ort in [1j*dir, -1j*dir]:
                    ins= current
                    while grid[ins] == ctype and grid[ins+dir] != ctype:
                        vis2.add((dir,ins+dir))
                        ins += ort
            elif neighbour not in visited: q.append(neighbour)
        area += 1
    tot+=len(vis2)*area
    tot2+=sides*area
print(tot)
print(tot2)


