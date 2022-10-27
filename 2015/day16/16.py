import itertools
import numpy as np
if __name__ == '__main__':
    with open('day16\input.txt') as file:
        data = file.read().splitlines()
    aunts = []
    for j in data:
        i = j.split()
        aunts.append([int(i[1][:-1]), int(i[3][:-1]), int(i[5][:-1]), int(i[7])])
    print(aunts)
