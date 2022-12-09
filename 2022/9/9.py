import numpy as np
import itertools
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)).split('2022')[0])
import aoctools

def in_range(pos_head, pos_tail):
    return True if 2 >=((pos_head[0] - pos_tail[0])**2 + (pos_head[1] - pos_tail[1])**2) else False

def move_to(pos_head, pos_tail):
    return [pos_tail[0] + np.sign(pos_head[0] - pos_tail[0]), pos_tail[1] + np.sign(pos_head[1] - pos_tail[1])]

def main():
    data = aoctools.data_loader(2022, 9, two_parts=False)
    visited = set()
    visited.add((0,0))
    pos_tails = [[0,0]]
    # num_tails = 1 # part 1
    num_tails = 9 # part 2
    for i in range(9):
        pos_tails.append([0,0])
    for i in data:
        ins = i.split(' ')
        for j in range(int(ins[1])):
            match ins:
                case 'U', x: pos_tails[0][1] += 1
                case 'D', x: pos_tails[0][1] -= 1
                case 'L', x: pos_tails[0][0] -= 1
                case 'R', x: pos_tails[0][0] += 1
            for i in range(1,num_tails+1):
                head, tail = pos_tails[i-1], pos_tails[i]
                if not in_range(head, tail):
                    pos_tails[i] = move_to(head, tail)
                    if i == num_tails: visited.add(tuple(pos_tails[i]))
    print(len(visited))
if __name__ == '__main__':
    main()