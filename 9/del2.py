def check_basin(basin, point):
    x = point[0]
    y = point[1]
    if basin[y][x] == 0:
        basin[y][x] = 1
        if x - 1 >= 0:
            left = check_basin(basin, [x - 1, y])
        else:
            left = 0
        if x + 1 < 100:
            right = check_basin(basin, [x + 1, y])
        else:
            right = 0
        if y + 1 < 100:
            under = check_basin(basin, [x, y + 1])
        else:
            under = 0
        if y - 1 >= 0:
            over = check_basin(basin, [x, y - 1])
        else:
            over = 0
        return 1 + over + under + left + right
    else:
        return 0


def main():
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
    basin = [[int(int(e) == 9) for e in i] for i in data]
    bas = []
    for i in range(100):
        for j in range(100):
            n = check_basin(basin, [i, j])
            if n != 0:
                bas.append(n)
    print(sorted(bas))

if __name__ == '__main__':
    main()
