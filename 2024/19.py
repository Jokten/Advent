import aoc
from functools import cache
data = aoc.get_data(2024,19).split("\n\n")
patt = tuple(data[0].split(", "))
des = data[1].split("\n")

@cache
def findpat(patt, p):
    cnt = 0
    for i in patt:
        if i == p: cnt += 1
        elif p.startswith(i): 
            cnt += findpat(patt, p[len(i):])
    return cnt

cnt = [findpat(patt, i) for i in des]
print(f"Part 1: {sum((i > 1 for i in cnt))} Part 2: {sum(cnt)}")
