import numpy as np

def expand_universe(universe):
    row_cnt = []
    col_cnt = []
    for i in range(len(universe)):
        if sum(universe[i]) == 0:
            row_cnt.append(i)
    for j in range(len(universe[0])):
        if sum(universe[:,j]) == 0:
            col_cnt.append(j)
    return row_cnt, col_cnt
def main():
    with open(r".\2023\11\input.txt", 'r') as f:
        data = f.readlines()
    data = [line.strip() for line in data]
    universe = []
    gal = 1

    for line in data:
        rw = []
        for char in line:
            if char == '#':
                rw.append(gal)
                gal += 1
            else:
                rw.append(0)
        universe.append(rw)
    universe = np.array(universe, dtype=np.int32)
    galaxies = np.unique(universe, return_index=True)[1]
    galaxies = [(i//len(universe[0]), i%len(universe[0])) for i in galaxies[1:]]
    sum_gal = 0
    sum_p2 = 0
    rws,cols = expand_universe(universe)
    for i in range(len(galaxies)-1):
        for j in range(i+1, len(galaxies)):
            dist = abs(galaxies[i][0]-galaxies[j][0])+abs(galaxies[i][1]-galaxies[j][1])
            x1,x2 = max(galaxies[i][0], galaxies[j][0]), min(galaxies[i][0], galaxies[j][0])
            y1,y2 = max(galaxies[i][1], galaxies[j][1]), min(galaxies[i][1], galaxies[j][1])
            p1 = 0
            p2 = 0
            for cl in cols:
                if y1>=cl>=y2:
                    p1 += 1
                    p2 += 1000000-1
            for rw in rws:
                if x1>=rw>=x2:
                    p1 += 1
                    p2 += 1000000-1
        
            sum_gal += dist + p1
            sum_p2 += dist + p2
    print(sum_gal)
    print(sum_p2)

    

if __name__ == '__main__':
    main()