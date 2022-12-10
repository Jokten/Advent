import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)).split('2022')[0])
import aoctools

def main():
    data = aoctools.data_loader(2022, 10, two_parts=False)
    cyc = 1
    sigs = []
    val = 1
    crt = []
    prevs = []

    for i in range(6):
        lis = []
        for j in range(40):
            lis.append(' ')
        crt.append(lis)

    while data:
        if (cyc-20)%40 == 0:
            sigs.append(int(val)*cyc)
        adj_val = max(0,val)
        if (cyc-1)%40 in [max(0,adj_val-1)%40, (adj_val)%40, (adj_val+1)%40]:
            if cyc == 40: print('val', val)
            crt[(cyc-1)//40][((cyc-1)%40)] = '#'
        cyc += 1        
        if prevs: val += int(prevs.pop(0))
        else: 
            cur = data.pop(0).split()
            if cur[0] == 'addx': prevs.append(cur[1])
    print(f'Part 1: {sum(sigs)}')
    for i in crt:
        print(''.join(i))
        
    
if __name__ == '__main__':
    main()