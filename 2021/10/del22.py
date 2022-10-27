from numpy import median


def main():
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
    start = ['(', '[', '{', '<']
    slut = [')', ']', '}', '>']
    scores = []
    for line in data:
        summa = 0
        stack = []
        for i in line:
            if i in start:
                index = start.index(i)
                stack.append(index)
            elif i in slut:
                index = slut.index(i)
                if index != stack.pop():
                    stack = []
                    break
        while len(stack) != 0:
            summa = 5*summa + stack.pop()+1
        if summa != 0:
            scores.append(summa)
    print(median(scores))


if __name__ == '__main__':
    main()
