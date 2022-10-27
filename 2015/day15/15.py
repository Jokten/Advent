import itertools
import numpy as np
if __name__ == '__main__':
    with open('day15\input.txt') as file:
        data = file.read().splitlines()
    cookies = {}
    for i in data:
        props = i.split()[::2]
        cookies[props[0][:-1]] = np.append(np.array([int(j[:-1]) for j in props[1:-1]]), [int(props[-1])])
    combs = itertools.combinations_with_replacement(cookies.keys(),100)
    print(cookies.values())
    best = 0
    for recipe in combs:
        result = np.zeros(4)
        calorie = 0
        for ingredient in recipe:
            d = cookies[ingredient]
            result += d[:-1]
            calorie += d[-1]
            if calorie > 500:
                break
        result[result < 0] = 0
        score = np.prod(result)
        if score > best and calorie == 500:
            best = score
    print(best)