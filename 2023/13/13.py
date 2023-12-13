import numpy as np

def main():
    with open(r'2023/13/input.txt') as f: data = f.read()
    data = [np.array([[1 if k == '#' else 0 for k in tr] for tr in i.splitlines()]) for i in data.split('\n\n')]
    p1, p2= 0, 0
    for i in data:
        p1 += solve(i, False)
        p2 += solve(i, True)
    print(f'Part 1: {p1}\nPart 2: {p2}')

def solve(land, p2=False):
    for i in range(1,land.shape[0]):
        mi = min(len(land[i:]), len(land[:i]))
        mir = np.flipud(land[:i])[:mi]
        if np.sum(land[i:i+mi]==mir) == np.prod(mir.shape)-p2: return i*100
        
    for i in range(1,land.shape[1]):
        mi = min(land[:,i:].shape[1], land[:,:i].shape[1])
        mir = np.fliplr(land[:,:i])[:,:mi]
        if np.sum(land[:,i:i+mi]==mir) == np.prod(mir.shape)-p2: return i
    
if __name__ == '__main__':
    main()