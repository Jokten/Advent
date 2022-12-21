import re
from functools import cache
import time
from itertools import chain, combinations
from tqdm import tqdm
from copy import deepcopy

def parse():
    paths = {}
    flow = {}
    with open(r'2022\16\input.txt', 'r') as openfile:
        data = openfile.read().splitlines()
    for i in data:
        k = re.findall(r'([A-Z]{2})', i)
        paths[k[0]]= k[1:]
        flow[k[0]] = int(re.findall(r'\d+', i)[0])
    return flow, paths

def non_zero(current):
    start = paths[current]
    pos = []
    turn = 1
    all = [current]
    while start:
        new_start = []
        for i in start:
            if i not in all:
                all.append(i)
                if flow[i] > 0:
                    pos.append((i,turn))
                new_start += paths[i]
                new_start += paths[i]
        turn += 1
        start = new_start
    return tuple(pos)


def checker(turn, current, on, TODO):
    possible = []
    turn -= 1
    prs = flow[current]*turn
    if on == TODO:
        return prs

    for i, j in paths[current]:
        if (i not in on) and (i in TODO) and (j < turn):
            possible.append(checker(turn-j, i, on +(current,),TODO))
    if possible:
        return max(possible)+prs
    else:
        return prs
            
#def main():
flow, paths = parse()
new_paths = {'AA': non_zero('AA')}
for i in paths:
    if flow[i] > 0: new_paths[i] = non_zero(i)

paths = new_paths
stat = time.perf_counter()
print(checker(30+1, 'AA', (),tuple(paths.keys())))
print(time.perf_counter()-stat)

scen = []
things = list(paths.keys())
things.remove('AA')
subs = list(chain.from_iterable(combinations(things, r) for r in range(len(things)+1)))
tot = len(subs)
for ss in tqdm(subs, total=tot):
    scen.append(checker(26+1,'AA',(),tuple(ss))+ checker(26+1,'AA',(),tuple(set(things)-set(ss))))
print(max(scen))

