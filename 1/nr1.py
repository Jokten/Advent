if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()

    data = list(map(lambda x: int(x), data))
    n = 0
    smoothdata = [sum(data[index:index+3]) for index, _ in enumerate(data) if index < len(data)-2]

    for i in range(len(smoothdata)-1):
        if smoothdata[i + 1] > smoothdata[i]:
            n += 1
    print(smoothdata)