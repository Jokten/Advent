import numpy as np
import itertools

look = {'X': 'A', 'Y': 'B', 'Z': 'C'}
conv = {'A': 0, 'B': 1, 'C': 2}
def load_data():
    with open("2022\\2\\input.txt", "r") as f:
        data = f.read().splitlines()
    return data

def calc_score(p1, p2):
    sc = p1 + 1
    if p1 == p2: sc += 3
    elif p1 == (p2+1)%3: sc += 6
    return sc

def part1(data):
    sc = 0
    for i in data:
        play2 = conv[i[0]]
        play1 = conv[look[i[1]]]
        sc += calc_score(play1, play2)
    return sc

def part2(data):
    sc = 0
    for i in data:
        play2 = conv[i[0]]
        play1 = (play2 + conv[look[i[1]]]-1)%3
        sc += calc_score(play1, play2)
    return sc

def main():
    d = load_data()
    D = [i.split(' ') for i in d]
    print(part1(D))
    print(part2(D))

if __name__ == "__main__":
    main()