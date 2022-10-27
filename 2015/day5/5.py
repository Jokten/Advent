if __name__ == '__main__':
    with open('day5\input.txt') as file:
        data = file.read().splitlines()
    forbidden = ['ab', 'cd', 'pq', 'xy']
    vowels = ['a','e','i','o','u']
    nice = 0
    for i in data:
        naughty = 0
        for j in forbidden:
            if j in i:
                naughty = 1
        counter = 0
        for v in vowels:
            counter += i.count(v)
        if counter < 3:
            naughty = 1
        double = 0
        for k in range(len(i)-1):
            if i[k] == i[k+1]:
                double = 1
        if double == 0:
            naughty = 1
        if naughty == 0:
            nice += 1


    print(nice)