from main import most_common

def main():
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
    oxygen = data.copy()
    n = 0
    while len(oxygen)>1:
        val = most_common(oxygen, n)
        oxygen = [i for i in oxygen if i[n] == val]
        n += 1
        print()
    c02 = data.copy()
    n = 0
    while len(c02)>1:
        val = most_common(c02, n)
        c02 = [i for i in c02 if i[n] is not val]
        n += 1
    print(c02)
    print(oxygen)
    ox = int(oxygen[0],2)
    c0 = int(c02[0], 2)
    print(ox*c0)

if __name__ == '__main__':
    main()