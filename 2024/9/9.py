f = list(map(int,open("./2024/9/input.txt", "r").read().strip()))
file = []
space = []
id = 0
for e, i in enumerate(f):
    if e%2: space.append(i)
    else:
        file.append([id, i])
        id += 1
final = []
space_d = [[] for i in space]
for e1, f in enumerate(reversed(file.copy())):
    ind = len(file)-e1-1
    for e, l in enumerate(space):
        if f[1] <= l and e < ind:
            for i in range(f[1]): space_d[e].append(f[0])
            space[e] -= f[1]

            file[ind] = [0, f[1]]
            break

print(space,"\n", space_d,"\n",file)
print(len(space),len(space_d), len(file))
while file:
    cc = file.pop(0)
    for i in range(cc[1]): final.append(cc[0])
    if space_d:
        final += (space_d.pop(0))
        for j in range(space.pop(0)): final += [0]

            
#5144981023042
#8444425634594
#6272188244509

while file:
    cur = space.pop(0)
    cc = file.pop(0)
    for i in range(cc[1]): final.append(cc[0])
    for i in range(cur):
        while file[-1][1] == 0:
            file.pop(-1)
        final.append(file[-1][0])
        file[-1][1] -= 1
        if file[-1][1] == 0:
            file.pop(-1)
s = 0

for e, i in enumerate(final): s+=e*i

print(s)

