import itertools
import numpy as np

def max_length(box):
    nog = 150
    b = sorted(box)
    for i in range(len(b)):
        if sum(b[:i]) > nog:
            return i
    

if __name__ == '__main__':
    with open('2015\day17\input.txt') as file:
        data = file.read().splitlines()
    boxes = [int(i) for i in data]
    max = 11
    combs = []
    count = 0
    min = 20
    for i in range(3,max):
        combs += list(itertools.combinations(boxes,i))
    for i in combs:
        if sum(i) == 150:
            if len(i) < min:
                count = 1
                min = len(i)
                print('heer')
            elif len(i) == min:
                count += 1
    print(count)
    print(min)

    