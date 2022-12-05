import numpy as np
import itertools


def load_data():
    with open("2022\\4\\input.txt", "r") as f:
        data = f.read().splitlines()
    stack = [[] for i in range(9)]
    for i in range(8):
        for j in range(9):
            if data[i][j*4+1] != ' ':
                stack[j].append(data[i][j*4+1])
    [i.reverse() for i in stack]
    inst = []
    for i in data[10:]:
        k = i.split(' ')
        inst.append((int(k[1]), int(k[3]), int(k[5])))
    print(stack)
    return stack, inst

def part1(data):
    stack = data[0]
    inst = data[1]
    for i in inst:
        for j in range(i[0]):
            stack[i[2]-1].append(stack[i[1]-1].pop())
    print(stack)
    for i in stack:
        print(i[-1], end='')

def part2(data):
    stack = data[0]
    inst = data[1]
    for i in inst:
        stack[i[2]-1] += stack[i[1]-1][-i[0]:]
        print(stack)
        for j in range(i[0]):
            stack[i[1]-1].pop()
    print(stack)
    for i in stack:
        print(i[-1], end='')

def main():
    d = load_data()
    print(part1(d))
    print(part2(load_data()))

if __name__ == "__main__":
    main()