import re
from functools import cache
import time

@cache
def get_turns(i, resources, robots):
    if 0 in [a*b for a, b in zip(i, robots) if a > 0]:
        res = 0
    else:
        m = max([((b-a)//c)+((b-a)%c != 0) for a, b, c in zip(resources, i, robots) if b > 0]+ [0])+1
        new_resources = tuple([a-b+c*(m) for a, b, c in zip(resources, i, robots)])
        res=(m,new_resources)
    return res

@cache
def get_geodes(blueprint, turn, resources, robots, max_robots):
    if turn == 0: return resources[3]
    else:
        current = []
        tt = []
        for e,i in enumerate(blueprint):
            if max_robots[e] > robots[e]:
                a = get_turns(i, resources, robots)
                if a == 0:
                    tt.append(0)
                else:
                    t, reso = a
                    reso = tuple([min(a,2*b) for a, b in zip(reso, max_robots)])
                    tt.append((t, reso))
            else:
                tt.append(0)
        if tt[-1] != 0 and tt[-1][0] == 1:
            if tt[-1][0] <= turn:
                new_robots = list(robots)
                new_robots[-1] = new_robots[-1]+1
                new_robots = tuple(new_robots)
                current.append(get_geodes(blueprint, turn-tt[-1][0], tt[-1][1], new_robots, max_robots))
        else:
            for e, i in enumerate(tt):
                if i != 0 and i[0] <= turn:
                    new_robots = list(robots)
                    new_robots[e] = new_robots[e]+1
                    new_robots = tuple(new_robots)
                    current.append(get_geodes(blueprint, turn-i[0], i[1], new_robots, max_robots))
        if current:
            return max(current)
        else:
            return resources[3] + robots[3]*turn
def main():
    r = r'Each ([a-z]+) robot costs ([0-9]+ [a-z]+)(?: and ([0-9]+ [a-z]+))?.'
    order = {'ore': 0, 'clay': 1, 'obsidian': 2}

    with open ("2022/19/input.txt", "r") as f:
        blue = f.read().splitlines()
    blueprints = []
    maxi = []
    for e, i in enumerate(blue):
        max_i = [0,0,0,1000]
        max_r = [0,0,0,1000]
        current = []
        data = re.findall(r, i)
        for robot in data:
            cost = [0, 0, 0, 0]
            for j in robot[1:]:
                if j:
                    max_i[order[j.split()[1]]] = max(int(j.split()[0]), max_i[order[j.split()[1]]])
                    cost[order[j.split()[1]]] = int(j.split()[0])
            current.append(tuple(cost))
        blueprints.append(tuple(current))
        maxi.append(tuple(max_i))
        

    robots = (1, 0, 0, 0)
    resources = (0, 0, 0, 0)
    stt = time.time()
    # part 1
    summ = 0
    for e, i in enumerate(blueprints, 1):
        maxii = maxi[e-1]
        start = time.time()
        aa = get_geodes(i, 24, resources, robots, maxii)
        end = time.time()
        get_geodes.cache_clear()
        get_turns.cache_clear()
        summ += e*aa
    print(summ)
    p1 = time.time()
    print(p1-stt)


    # part 2
    s = 1
    for e, i in enumerate(blueprints[:3], 1):
        maxii = maxi[e-1]
        aa = get_geodes(i, 32, resources, robots, maxii)
        end = time.time()
        get_geodes.cache_clear()
        get_turns.cache_clear()

        s *= aa
    print(s)
    p2 = time.time()
    print(p2-p1)
    

main()
        
        