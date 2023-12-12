import re

def main():
    with open(r".\2023\9\input.txt") as f:
        data = f.readlines()
        lines = [[int(i) for i in re.findall(r'-?\d+', row)] for row in data]
    s = 0
    s2 = 0
    for i in lines:
        rows = [i]
        while sum([abs(x) for x in rows[-1]]) != 0:
            next = []
            for ind in range(len(rows[-1])-1):
                next.append(rows[-1][ind+1]-rows[-1][ind])
            rows.append(next)
        start = 0
        startsp2 = 0
        for ind in range(len(rows)):
            start += rows[-1-ind][-1]
            startsp2 = rows[-1-ind][0] - startsp2
        s += start
        s2 += startsp2

    print(f'Part 1: {s}')
    print(f'Part 2: {s2}')
if __name__ == "__main__":
    main()