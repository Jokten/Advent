import numpy as np
import re

def parser():
    with open(r'2022\14\input.txt', 'r') as openfile:
        data = openfile.read().splitlines()
    rocks = set()
    for row in data:
        r = []
        row = row.split(' -> ')
        for cords in row:
            cords = cords.split(',')
            cords = [int(i) for i in cords]
            r.append(tuple(cords))
        for k in range(len(r)-1):
            upx = max([r[k][0], r[k+1][0]])
            downx = min([r[k][0], r[k+1][0]])
            upy = max([r[k][1], r[k+1][1]])
            downy = min([r[k][1], r[k+1][1]])
            for i in range(downx, upx+1):
                for j in range(downy, upy+1):
                    rocks.add((i, j))
    return rocks

def neighbours(cords):
    if 
            
    # 169

def main():
    data = parser()
    

if __name__ == '__main__':
    main()