def main():
    with open('input.txt', 'r') as file:
        data = file.readline()
        position = [int(i) for i in data.split(',')]
    fuel = []
    for i in range(1000):
        fuel.append(sum([sum(range(1, abs(j-i)+1)) for j in position]))
    print(min(fuel))


if __name__ == '__main__':
    main()
