import numpy as np

def main():
    with open(r'2023/13/input.txt') as f: data = f.read()
    data = data.split('\n\n')
    data = [np.array([[1 if k == '#' else 0 for k in tr] for tr in i.splitlines()]) for i in data]
    p1, p2= 0, 0
    for i in data:
        p1 += solve(i, True)
        p2 += solve(i)
    print(p1)
    print(p2)

def solve(land, p1=False):
    for i in range(1,land.shape[0]):
        mi = min(len(land[i:]), len(land[:i]))
        mir = np.flipud(land[:i])[:mi]
        li = land[i:i+mi]
        if p1 and np.array_equal(li, mir): return i*100
        elif np.sum(li==mir) == np.prod(mir.shape)-1: return i*100
        
    for i in range(1,land.shape[1]):
        mi = min(land[:,i:].shape[1], land[:,:i].shape[1])
        mir = np.fliplr(land[:,:i])[:,:mi]
        li = land[:,i:i+mi]
        if p1 and np.array_equal(li, mir): return i
        elif np.sum(li==mir) == np.prod(mir.shape)-1: return i
    
    

if __name__ == '__main__':
    main()