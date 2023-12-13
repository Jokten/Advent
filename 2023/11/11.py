import itertools

def main():
    with open('2023/11/input.txt') as f: data = f.readlines()
    data = [list(i.strip()) for i in data]
    rows, cols, gal = set(), set(), []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '#': gal.append((i,j))
        if '#' not in data[i]: rows.add(i)
        if '#' not in [j[i] for j in data]: cols.add(i)

    p1, p2 = 0, 0

    for g1, g2 in itertools.combinations(gal, 2):
        dist = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
        r = sum(1 for i in rows if min(g1[0], g2[0]) < i < max(g1[0], g2[0]))
        c = sum(1 for i in cols if min(g1[1], g2[1]) < i < max(g1[1], g2[1]))
        p1 += dist + r + c
        p2 += dist + (r + c)*999999
    print(f'Part 1: {p1}\nPart 2: {p2}')
            
if __name__ == '__main__':
    main()


