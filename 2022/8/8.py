import numpy as np
import itertools
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)).split('2022')[0])
import aoctools

def tree_check(data,reverse=False, transpose=False):
    trees = []
    for y, row in enumerate(data):
        if reverse: row = row[::-1]
        prev = -1
        for x,  tree in enumerate(row):
            if tree > prev:
                    prev = int(tree)
                    if transpose: 
                        if reverse:
                            trees.append((y,len(row)-x-1))
                        else: trees.append((y,x))
                    else:
                        if reverse: 
                            trees.append((len(row)-x-1,y))
                        else: trees.append((x,y))
    return trees

def scenic(forest, x, y):
    if x in [0, 98] or y in [0, 98]:
        return 0
    up = forest[y-1::-1,x]
    down = forest[y+1:,x]
    left = forest[y, x-1::-1]
    right = forest[y, x+1:]
    dirs = [up, down, left, right]
    scores  = []
    for i in dirs:
        score = 0
        for trees in i:
            if trees < forest[y][x]: 
                score+=1
            else: 
                score += 1 
                break
        scores.append(score)
    total = 1
    for i in scores:
        total *= i
    return total

def main():
    data = aoctools.data_loader(2022, 8, two_parts=False)
    forest = []
    for row in data:
        forest.append([int(i) for i in list(row)])
    forest = np.array(forest)

    cnt = tree_check(forest)
    cnt += tree_check(forest, reverse=True)
    cnt += tree_check(forest.T, transpose=True)
    cnt += tree_check(forest.T, reverse=True, transpose=True)
    print(len(set(cnt))) # part 1

    leng = forest.shape[0]
    cords = itertools.product(range(leng), repeat=2)
    scores = []
    for i in cords:
        scores.append(scenic(forest, i[0], i[1]))
    print(max(scores)) # part 2

if __name__ == "__main__":
    main()