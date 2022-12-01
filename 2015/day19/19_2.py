import itertools
import numpy as np
import heapq

def mol_div(s):
    ls = []
    st = ''
    for i in s:
        if i.isupper():
            if st:
                ls.append(st)
            st = i
        else:
            st += i
    ls.append(st)
    return ls

def ancestor(s1, d):
    x = [(len(s1), s1, 0)]
    anc = []
    print(x)
    tested = set()
    while x:
        kj = heapq.heappop(x)
        s = kj[1]
        reduced = 1
        for i in tr.items():
            for j in i[1]:
                gh = s.split(j)
                for k in range(1,len(gh)):
                    ss = j.join(gh[:k]) + i[0] + j.join(gh[k:])
                    if ss not in tested:
                        reduced = 0
                        heapq.heappush(x,(len(ss), ss, kj[2]+1))
                        tested.add(ss)
        if reduced and ((len(mol_div(s)) <= d+1) or s == 'e'):
            anc.append((s,kj[2]))
    print(anc)
    return anc



def trans(dat):
    tra = {}
    for i in dat[:-2]:
        d = i.split(' => ')
        if d[0] not in tra.keys():
            tra[d[0]] = [d[1]]
        else:
            tra[d[0]].append(d[1])
    return tra

def submols(s):
    ss = mol_div(s)
    subs = []
    cur = ''
    c = 0
    for i in ss:
        if i == 'Rn':
            c += 1
            cur += i
            
        elif i == 'Ar':
            c -= 1
            cur += i
            if c == 0:
                subs.append(cur)
                cur = ''
        else:
            cur += i
    return subs        




if __name__ == '__main__':
    with open('2015\day19\input.txt') as file:
        data = file.read().splitlines()
    tested = set()
    tr = trans(data)
    start = data[-1]
    sub = submols(start)
    total = 0
    new = ''
    print(sub)
    print(len(mol_div(start)))
    brea
    for i in sub:
        re = ancestor(new+i,len(mol_div(new)))
        new = re[0][0]
        total += re[0][1]
        print(new)
        print(total)
    
    
    