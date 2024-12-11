import aoc
d = {int(a)+int(b)*1j: int(col) for a, row in enumerate(aoc.get_data(2024, 10).split("\n")) for b,col in enumerate(row)}
tot = set()
p1, p2 = 0, 0
for i in d:
    if d[i] != 0: continue
    q = [i]
    while q:
        c = q.pop()
        if d[c] == 9:
            p2 += 1
            tot.add(c)
        for i in [-1, 1, -1j, 1j]:
            if c+i in d and d[c+i] == d[c]+1: 
                q.append(c+i)
    p1 += len(tot)
    tot = set()
print(p1, p2)

