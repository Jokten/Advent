import itertools

with open ("2022\\18\\input.txt", "r") as f:
    data = f.read().splitlines()
data = [tuple(map(int, i.split(','))) for i in data]
drop = set(tuple(data))

def neighbours(x, y, z):
    return [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)]

box_size = 22
out = set()
for x,y,z in itertools.product(*[list(range(-1, box_size)) for j in range(3)]):
    if -1 in (x, y, z) or box_size-1 in (x, y, z) and (x, y, z) not in out:
        out.add((x, y, z))
        outer = [(x,y,z)]
        while outer:
            x, y, z = outer.pop()
            for i in neighbours(x, y, z):
                if i not in drop and -2 not in i and box_size not in i and i not in out:
                    out.add(i)
                    outer.append(i)

tot = 0
for i in data:
    exp = 6
    for j in neighbours(*i):
        if j not in out:
            exp-=1
    tot+=exp

print(tot)