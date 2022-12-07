import numpy as np
import itertools
import sys
import os
import re
import copy
sys.path.append(os.path.dirname(os.path.realpath(__file__)).split('2022')[0])
import aoctools


def part1(data):
    data = data[0]
    last_4 = list(data[:4])
    for i in range(4, len(data)):
        daT = set(last_4)
        if len(daT) == 4:
            return i
        last_4.pop(0)
        last_4.append(data[i])

def part2(data):
    data = data[0]
    last_4 = list(data[:14])
    for i in range(14, len(data)):
        daT = set(last_4)
        if len(daT) == 14:
            return i
        last_4.pop(0)
        last_4.append(data[i])

def main():
    data = aoctools.data_loader(2022, 6, two_parts=False)
    print(data)
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()