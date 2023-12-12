from functools import cache
import time

@cache
def r(i, g):    
    if len(g) == 0: return not len(i) or '#' not in i
    if g[0] > len(i): return 0
    if g[0] == len(i) and '.' not in i: return 1 if len(g) == 1 else 0
    
    match i[0]:
        case '#': return r(i[g[0]+1:], g[1:]) if '.' not in i[0:g[0]] and i[g[0]]  in ['.', '?'] else 0
        case '.': return r(i[1:], g)
        case '?': return r('#' + i[1:], g) + r(i[1:], g)
          
def main():
    with open('2023/12/input.txt') as f: data = f.readlines()
    data = [i.strip().split(' ') for i in data]
    p1,p2 = 0,0
    for i in data:
        groups = tuple([int(j) for j in i[1].split(',')])
        p1 += r(i[0], groups)
        p2 += r(i[0] + ('?' + i[0])*4, groups*5)
    print(f'Part 1: {p1}\nPart 2: {p2}')

if __name__ == '__main__':
    start = time.time()
    main()
    print(f'Took {time.time() - start}')