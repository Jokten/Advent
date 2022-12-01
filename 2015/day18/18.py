import itertools
import numpy as np

def update(grid):
    kord = range(1,101)
    cords = itertools.product(kord, repeat=2)
    new_grid = np.zeros((102,102))
    for i in cords:
        c = c_n(i, grid)
        if grid[i[0],i[1]] == 1 and c in [2,3]:
            new_grid[i[0],i[1]] = 1
        elif grid[i[0],i[1]] == 0 and c == 3:
            new_grid[i[0],i[1]] = 1
    return new_grid
        

def c_n(point, grid):
    x, y = point
    return sum(grid[x-1:x+2, y-1]) + sum(grid[x-1:x+2, y+1]) + grid[x-1, y] + grid[x+1, y] 

if __name__ == '__main__':
    with open('2015\day18\input.txt') as file:
        f = file.read().splitlines()
    n = len(f[0])
    grid = np.zeros((n+2,n+2))
    
    for e, i in enumerate(f):
        grid[e+1,1:-1] = [k=='#' for k in i]
    grid[1,1] = grid[1,n] = grid[n,1] = grid[n,n] = 1
    # for k in grid[1:-1,1:-1]:
    #     s = ''
    #     for j in k:
    #         if j == 1:
    #             s += '#'
    #         else:
    #             s += '.'
    #    print(s)
    print('\n')
    for i in range(100):
        grid = update(grid)
        grid[1,1] = grid[1,n] = grid[n,1] = grid[n,n] = 1
        # for k in grid[1:-1,1:-1]:
        #     s = ''
        #     for j in k:
        #         if j == 1:
        #             s += '#'
        #         else:
        #             s += '.'
        #     print(s)
        # print('\n')
    print(sum(sum(grid)))
    print(grid)