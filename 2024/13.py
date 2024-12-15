import aoc
import numpy as np
import re
data = aoc.get_data(2024,13)
vspaces = [[list(map(int,re.findall(r"\d+", i ))) for i in space.split("\n")]for space in data.split("\n\n")]

for p in [0, 1]:
    toks = 0
    for vs in vspaces:
        A = np.array(vs[0:2], dtype=np.int64).transpose()
        b = np.array(vs[2], dtype=np.int64)
        if p: b = np.add(np.array([10000000000000, 10000000000000], dtype=np.int64), b)
        x = np.linalg.solve(A,b).round()
        if (A @ x == b).all():
            toks += x[0]*3 + x[1]
    print(int(toks))
