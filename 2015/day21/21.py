import itertools
import numpy as np


def main():
    with open('2015\day21\input.txt') as file:
        data = file.read().splitlines()[1:]
    weapons = {}
    armors = {}
    rings = {}
    for i in data[:5]:
        d = i.split(' ')
        d = [j for j in d if j]
        weapons[d[0]] = [int(d[1]), int(d[2]), int(d[3])]
    for i in data[7:11]:
        d = i.split(' ')
        d = [j for j in d if j]
        armors[d[0]] = [int(d[1]), int(d[2]), int(d[3])]
    for i in data[14:]:
        d = i.split(' ')
        d = [j for j in d if j]
        rings[d[0] + d[1]] = [int(d[2]), int(d[3]), int(d[4])]
    armors['None'] = [0, 0, 0]
    rings['None'] = [0, 0, 0]
    rings['None2'] = [0, 0, 0]
    # Gives combinations of weapons, armors and rings
    comb = list(itertools.product(weapons.keys(), armors.keys(), rings.keys(), rings.keys()))
    # Remove combinations where the same ring is used twice
    comb = [i for i in comb if i[2] == 'None' or i[2] != i[3]]
    boss = [100, 8, 2]
    min_cost = 100000
    # Part 1
    for i in comb:
        cost = weapons[i[0]][0] + armors[i[1]][0] + rings[i[2]][0] + rings[i[3]][0]
        attack = weapons[i[0]][1] + armors[i[1]][1] + rings[i[2]][1] + rings[i[3]][1]
        armor = weapons[i[0]][2] + armors[i[1]][2] + rings[i[2]][2] + rings[i[3]][2]
        p1 = np.ceil(boss[0]/max(1, attack-boss[2]))
        p2 = np.ceil(100/max(1, boss[1]-armor))
        if p1 <= p2:
            if cost < min_cost:
                min_cost = cost
    print(min_cost)

    # Part 2
    max_cost = 0
    for i in comb:
        cost = weapons[i[0]][0] + armors[i[1]][0] + rings[i[2]][0] + rings[i[3]][0]
        attack = weapons[i[0]][1] + armors[i[1]][1] + rings[i[2]][1] + rings[i[3]][1]
        armor = weapons[i[0]][2] + armors[i[1]][2] + rings[i[2]][2] + rings[i[3]][2]
        p1 = np.ceil(boss[0]/max(1, attack-boss[2]))
        p2 = np.ceil(100/max(1, boss[1]-armor))
        if p1 > p2:
            if cost > max_cost:
                max_cost = cost
    print(max_cost)

if __name__ == '__main__':
    main()