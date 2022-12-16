import re
from functools import cache

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

@cache
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
                else:
                    done = 1
                    new_start += paths[i]
        turn += 1
        start = new_start
    return tuple(pos)

@cache
def checker(turn, current, on):
    possible = []
    turn -= 1
    if turn == 0:
        return 0
    else:
        if current not in on and flow[current] > 0:
            possible.append(checker(turn, current, on+(current,))+flow[current]*turn)
            
        for i in paths[current]:
            possible.append(checker(turn, i, on))
    
    return max(possible)

@cache
def checker2(turn, turnelp, current, elph, on):
    possible = []
    if sorted(list(paths.keys())) == sorted(list(on)):
        return 0
    if turn < 0 or turnelp < 0:
        print(turn, turnelp, current, elph, on)
    if turnelp < turn:
        if turn == 0:
            return 0
        else:
            if current not in on:
                possible.append(checker2(turn-1, turnelp, current, elph, on+(current,))+flow[current]*turn)
            for i,j in paths[current]:
                if j > turn: continue
                possible.append(checker2(turn-j, turnelp, i, elph, on))
    else:
        if turnelp == 0:
            return 0
        if elph not in on and turnelp:
            possible.append(checker2(turn, turnelp-1, current, elph, on+(elph,))+flow[elph]*turnelp)
            
        for i, j in paths[elph]:
            if j > turnelp: continue
            possible.append(checker2(turn, turnelp-j, current, i, on))
    if possible:
        return max(possible)
    else:
        return 0

#def main():
flow, paths = parse()
new_paths = {'AA': non_zero('AA')}
new = {}
while True:
    done = 1
    for i in new_paths:
        for j in new_paths[i]:
            if j[0] not in new_paths:
                done = 0
                new[j[0]] = non_zero(j[0])
    new_paths.update(new)
            
    if done:
        break
paths = new_paths
new_flow = {}
#print(checker(30, 'AA', ()))
print(checker2(25, 25, 'AA', 'AA', ()))
# if __name__ == '__main__':
#     main()

