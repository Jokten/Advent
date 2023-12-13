from functools import cache
import time

# @cache
def r(i, g):    
    if len(g) == 0: return not len(i) or '#' not in i
    if g[0] > len(i): return 0
    if g[0] == len(i) and '.' not in i: return len(g) == 1
    
    match i[0]:
        case '#': return r(i[g[0]+1:], g[1:]) if '.' not in i[:g[0]] and i[g[0]]  != '#' else 0
        case '.': return r(i[1:], g)
        case '?': return (r(i[g[0]+1:], g[1:]) if '.' not in i[:g[0]] and i[g[0]]  != '#' else 0) + r(i[1:], g)
          
def main():
    with open('2023/12/input.txt') as f: data = f.readlines()
    data = [i.strip().split(' ') for i in data]
    p1,p2 = 0,0
    it = 0
    for i in data:
        it += 1
        print(it)
        li = '.'.join([j for j in i[0].split('.') if j])
        groups = tuple([int(j) for j in i[1].split(',')])
        p1 += r(li, groups)
        p2 += r(li + ('?' + li)*4, groups*5)
    print(f'Part 1: {p1}\nPart 2: {p2}')

if __name__ == '__main__':
    start = time.time()
    main()
    print(f'Took {time.time() - start}')