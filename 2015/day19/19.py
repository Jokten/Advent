import itertools
import numpy as np

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


if __name__ == '__main__':
    with open('2015\day19\input.txt') as file:
        data = file.read().splitlines()
    tr = {}
    start = data[-1]
    for i in data[:-2]:
        d = i.split(' => ')
        if d[0] not in tr.keys():
            tr[d[0]] = [d[1]]
        else:
            tr[d[0]].append(d[1])
    div = mol_div(start)
    res = set()
    for e, i in enumerate(div):
        if i in tr.keys():
            divc = div.copy()
            for j in tr[i]:
                divc[e] = j
                res.add(''.join(divc))
    print(len(res))
    