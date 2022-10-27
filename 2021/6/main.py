def main():
    with open('input.txt', 'r') as file:
        data = file.readline()
    d = data.split(',')
    fish = [0]*9
    for i in d:
        e = int(i)
        fish[e] += 1
    fish.reverse()
    for i in range(256):
        new_fish = [fish[e-1] for e in range(9)]
        new_fish[2] += fish[8]
        fish = new_fish
        print(fish)
    print(sum(fish))


if __name__ == '__main__':
    main()
