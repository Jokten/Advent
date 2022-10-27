import numpy as np
import itertools
if __name__ == '__main__':
    with open('day13\input.txt') as file:
        data = file.read().splitlines()
    people= set()
    haps = {}
    for i in data:
        j = i.split(' ')
        people.add(j[0])
        haps[(j[0],j[-1][:-1])] = (-1 + 2*(j[2] == 'gain')) * int(j[3])
    best = 0
    arr = ""
    for i in people:
        haps[('me',i)] = haps[(i,'me')] = 0
    people.add('me')
    for i in itertools.permutations(people):
        hapi = 0
        for j in range(len(i)-1):
            hapi += haps[(i[j],i[j-1])] + haps[(i[j],i[j+1])]
        hapi += haps[(i[-1],i[0])] + haps[(i[-1],i[-2])]
        if hapi > best:
            best = hapi
            arr = i
            print(best)
    print(best)
    print(i)
