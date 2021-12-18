def main():
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
    summa = 0
    uncorrupt = data.copy()
    for line in data:
        start = ['(','[','{','<']
        slut = [')',']','}','>']
        stack = []
        for i in line:
            if i in start:
                index = start.index(i)
                stack.append(index)
            elif i in slut:
                index = slut.index(i)
                if index != stack.pop():
                    summa += [3, 57, 1197, 25137][index]
                    break
    print(summa)
if __name__ == '__main__':
    main()
