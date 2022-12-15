import re
import numpy as np
import time

def find_possible(y,dists):
    ran = []
    for i,j in dists.items():
        if abs(y-i[1]) <= j:
            diff = abs(y-i[1])-j
            ren = (i[0]+diff, i[0]-diff)
            print(ren)
            if ran == []:
                print('onve')
                ran.append(ren)
            new_ran = ran.copy()
            to_remove = []
            for i in ran:
                print('here',i)
                if i[0] <= ren[0] <= i[1] or i[0] <= ren[1] <= i[1]:
                    to_remove.append(i)
                    new_ran.append((min(i[0], ren[0]), max(i[1], ren[1])))
                    break
                else:
                    ran.append(ren)
            print('ran',new_ran)
            print('rem',to_remove)
            for i in to_remove:
                new_ran.remove(i)
            ran = new_ran
            print(ran)
    s = 0
    print(ran)
    for i in ran:
        s += i[1]-i[0]+1
    print(s)

def main():
    with open(r'2022\15\input.txt', 'r') as openfile:
        data = openfile.read().splitlines()
    data = [re.findall(r'-?\d+', i) for i in data]
    beac = {}
    dists = {}
    thousand = set()
    ref = 2000
    for i in data:
        beac[(int(i[0]),int(i[1]))] = (int(i[2]), int(i[3]))
        dists[(int(i[0]),int(i[1]))] = abs(int(i[0])-int(i[2])) + abs(int(i[1])-int(i[3]))
    bc = set(beac.values())

    # for i in dists:
    #     diff =   abs(ref-i[1])
    #     if diff < dists[i]:
    #         for j in range(dists[i]-diff+1):
    #             thousand.add((i[0]+j, ref))
    #             thousand.add((i[0]-j, ref))
    # print(thousand.intersection(bc))
    # print(len(thousand))
    # print(len(thousand)-len(thousand.intersection(bc)))
    find_possible(10, dists)
        
    
            
if __name__ == '__main__':
    main()
