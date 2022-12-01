import itertools
import numpy as np
if __name__ == '__main__':
    with open('2015\day16\input.txt') as file:
        data = file.read().splitlines()
    aunts = []
    props = set()
    for j in data:
        i = j.replace(',','').replace(':','').split()
        for k in i[2::2]:
            props.add(k)
    for j in data:
        i = j.replace(',','').replace(':','').split()
        aunt = {}
        for k in props:
            aunt [k] = 0
        aunt[i[2]] = int(i[3])
        aunt[i[4]] = int(i[5])
        aunt[i[6]] = int(i[7])
        print(i)
        aunts.append([i[1], aunt])
    greater = ['cats','trees']
    less = ['pomeranians','goldfish']
    correct = [['children', 3],['cats', 7],['samoyeds', 2],['pomeranians', 3], ['goldfish', 5], ['trees', 3], ['cars', 2], ['perfumes', 1]]
    for a in aunts:
        d = a[1]
        cor = 0
        for i in correct:
            v = d[i[0]]
            if i[0] in greater:
                if v>i[1]:
                    cor += 1
                elif v!=0:
                    cor = 0
                    break
            elif i[0] in less:
                if v<i[1] and (v!=0):
                    cor += 1
                elif v!=0:
                    cor = 0
                    break
            else:
                if v==i[1]:
                    cor += 1
                elif v!=0:
                    cor = 0
                    break
        if cor > 2:
            print(a[0])
            print(d)
