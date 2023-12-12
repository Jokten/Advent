import re

def main():
    with open(r".\2023\4\input.txt") as f:
        lines = f.readlines()
    data = [[int(i) for i in re.findall(r'-?\d+', row)] for row in lines]
    points = 0
    count = [1 for i in range(len(data))]
    for i in data:
        win = set(i[1:11])
        have = set(i[11:])
        if len(win.intersection(have)) != 0:
            points += 2**(len(win.intersection(have))-1)
            for j in range(len(win.intersection(have))):
                count[i[0]+j] += count[i[0]-1]
    print(points)
    print(sum(count))

if __name__ == "__main__":
    main()
