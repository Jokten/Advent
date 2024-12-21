import heapq, aoc
from functools import cache

key = {'7': (0, 0), '8': (0, 1), '9': (0, 2), 
          '4': (1, 0), '5': (1, 1), '6': (1, 2), 
          '1': (2, 0), '2': (2, 1), '3': (2, 2), 
                       '0': (3, 1), 'A': (3, 2)}
c2d = {(0,1):(-1,0), (0,2):(0,0), (1,2):(0,1),(1,0):(0,-1), (1,1):(1,0)}

@cache
def cont(layer, sbut, ebut, keyp=0): 
    if layer == 0: return 1 
    q = [(0,sbut, (0,2))] 
    space = key.values() if keyp else c2d.keys()
    while q:
        s, c, pd = heapq.heappop(q) 
        if c == ebut: return max(s, cont(layer-1, pd, (0,2)))
        for d in ((0,1), (1,0), (1,1), (1,2)): 
            nex  = c[0]+c2d[d][0], c[1]+c2d[d][1]
            if nex not in space: continue
            cost = s + cont(layer-1, pd, d)
            if nex == ebut: cost += cont(layer-1, d, (0,2))
            heapq.heappush(q,(cost, nex, d)) 

data = aoc.get_data(2024,21).split("\n")
tot3 = tot26 = 0
for c in data:
    for e in range(len(c)):
        tot3 += int(c[:-1])*cont(3, key[c[e-1]], key[c[e]], 1)
        tot26 += int(c[:-1])*cont(26, key[c[e-1]], key[c[e]], 1)

# One line versions
#tot3 = sum(int(code[:-1])*sum(cont(3, keypad[code[e-1]], keypad[code[e]], 1) for e in range(len(code))) for code in data)
#tot26 = sum(int(code[:-1])*sum(cont(26, keypad[code[e-1]], keypad[code[e]], 1) for e in range(len(code))) for code in data)
print(tot3, tot26)