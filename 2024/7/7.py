import re
import time

def f(id,v,s,p):
    if id== len(v): return s==v[0]
    if s > v[0]: return 0
    if f(id+1, v, s+v[id], p): return 1
    if f(id+1, v, s*v[id], p): return 1
    if p and f(id+1, v, s*10**(len(str(v[id]))) + v[id], p): return 1

t = time.time()
d = [tuple(map(int,re.findall(r"\d+", i))) for i in open("./2024/7/input.txt", 'r').readlines()]
print(sum(i[0] for i in d if f(2,i, i[1], 0)),time.time()-t)
print(sum(i[0] for i in d if f(2,i, i[1], 1)),time.time()-t)
