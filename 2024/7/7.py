import itertools, re

def mult(a,b): return a*b
def add(a,b): return a+b
def con(a,b): return int(str(a) + str(b))

symbs = [mult, add, con]


d = [list(map(int,re.findall(r"\d+", i))) for i in open("input.txt", 'r').readlines()]
su = 0
for e, i in enumerate(d):
    print(e)
    end = int(i[0])
    for j in list(itertools.product(symbs, repeat=len(i)-2)):
        s = i[1]
        for k in range(len(j)):
            s = j[k](s,i[k+2])
            if s > end: break
        if s == end:
            su += end
            break
print(su)