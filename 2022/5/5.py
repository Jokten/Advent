import numpy as np
import itertools
import sys
import os
import copy
sys.path.append(os.path.dirname(os.path.realpath(__file__)).split('2022')[0])
import aoctools


def load_data():
    start_data, inst_data = aoctools.data_loader(2022, 5, two_parts=True)
    stack = [[] for i in range(9)]
    for i in range(8):
        for j in range(9):
            if start_data[i][j*4+1] != ' ':
                stack[j].append(start_data[i][j*4+1])
    for i in stack: i.reverse()
    
    inst = aoctools.parse_numbers(inst_data)
    return stack, inst

def part1(data):
    stack = copy.deepcopy(data[0])
    inst = data[1].copy()
    for i in inst:
        for j in range(i[0]):
            stack[i[2]-1].append(stack[i[1]-1].pop())
    st = ''
    for i in stack:
        st += i[-1]
    return st

def part2(data):
    stack = copy.deepcopy(data[0])
    inst = data[1].copy()
    for i in inst:
        stack[i[2]-1] += stack[i[1]-1][-i[0]:]
        for j in range(i[0]):
            stack[i[1]-1].pop()
    st = ''
    for i in stack:
        st += i[-1]
    return st

def main():
    d = load_data()
    print(part1(d))
    print(part2(d))

if __name__ == "__main__":
    main()