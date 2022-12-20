import numpy as np
with open(r"2022/20/input.txt", "r") as f:
    data = f.read().splitlines()
mod = len(data)
data = [int(i)*811589153 for i in data]
data = [i + e*mod for e, i in enumerate(data)]
assert len(data) == len(set(data))
array = data.copy()
for i in range(10):
    for e, j in enumerate(data):
        i = j - e*(mod)
        ind = array.index(j)
        array.pop(ind)
        array.insert((ind+i)%(mod-1),j)
array = [i-data.index(i)*mod for i in array]
zero = array.index(0)
ans = array[(zero+1000)%mod]+array[(zero+2000)%mod]+ array[(zero+3000)%mod]
print(ans)