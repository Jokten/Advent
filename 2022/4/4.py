def data_Reader():
    with open('2022\\4\\input.txt') as file:
        data = file.read().splitlines()
    return data

def part1(da):
    cnt = 0
    d = [[list(map(int, k)) for k in [dat.split('-') for dat in data.split(',')]] for data in da]
    for ass in d:
        first = set(range(ass[0][0], ass[0][1]+1))
        second = set(range(ass[1][0], ass[1][1]+1))
        if first & second == first or first & second == second:
            cnt += 1
    print(cnt)

def part2(da):
    cnt = 0
    d = [[list(map(int, k)) for k in [dat.split('-') for dat in data.split(',')]] for data in da]
    for ass in d:
        first = set(range(ass[0][0], ass[0][1]+1))
        second = set(range(ass[1][0], ass[1][1]+1))
        if first & second:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    data = data_Reader()
    part1(data)
    part2(data)