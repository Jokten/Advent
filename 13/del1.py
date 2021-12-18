import numpy as np


def fold(paper, line):
    if line[0] != 0:
        linje = line[0]
        ny_x = linje+1
        print(ny_x)
        x = ny_x * ['.']
        new_paper = []
        for i in range(len(paper)):
            new_paper.append(x.copy())
        for i in range(len(paper)):
            for j in range(len(paper[0])):
                if paper[i][j] == '#':
                    new_paper[i][linje-abs(linje - j)] = '#'

    if line[1] != 0:
        linje = line[1]
        ny_y = linje+1
        x = len(paper[0]) * ['.']
        new_paper = []
        for i in range(ny_y):
            new_paper.append(x.copy())

        for i in range(len(paper)):
            for j in range(len(paper[0])):
                if paper[i][j] == '#':
                    print()
                    new_paper[linje - abs(linje - i)][j] = '#'

    return new_paper


def main():
    folds = [[655, 0], [0, 447], [327, 0], [0, 223], [163, 0], [0, 111], [81, 0], [0, 55], [40, 0], [0, 27], [0, 13], [0, 6]]
    #folds = [[0,7],[5,0]]
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
    i = data[0]
    n = 0
    dots = []
    while i != '':
        dots.append([int(j) for j in i.split(',')])
        n += 1
        i = data[n]
    line = 1500 * ['.']
    paper = []
    for i in range(1500):
        paper.append(line.copy())
    print(dots)
    for i in dots:
        paper[i[1]][i[0]] = '#'
    for i in folds:
        for k in paper:
            for j in k:
                print(j, end='')
            print()
        print()
        paper = fold(paper, i)


    folded = paper

    count = 0
    for i in range(len(folded)):
        for j in range(len(folded[0])):
            if folded[i][j] == '#':
                count += 1
    for i in folded:
        for j in i:
            print(j, end='')
        print()
    print(count)


if __name__ == '__main__':
    main()
