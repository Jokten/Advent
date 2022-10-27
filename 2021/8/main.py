import numpy as np
def main():
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
        digits = [[j.split(' ') for j in i.split(' | ')] for i in data]
    summa = 0
    for i in digits:
        numbers = {}
        len_dig = [len(j) for j in i[0]]
        numbers[1] = set(i[0][len_dig.index(2)])
        numbers[4] = set(i[0][len_dig.index(4)])
        numbers[7] = set(i[0][len_dig.index(3)])
        numbers[8] = set(i[0][len_dig.index(7)])

        for j in i[0]:
            if set(j) == numbers[1]:
                pass
            elif set(j) == numbers[4]:
                pass
            elif set(j) == numbers[7]:
                pass
            elif set(j) == numbers[8]:
                pass
            elif len(set(j)-numbers[7])==2:
                numbers[3]=set(j)
            elif len(j) == 6 and len(set(j)-numbers[7]) == 3 and len(set(j)-numbers[4]) == 3:
                numbers[0] = set(j)
            elif len((set(j) - numbers[7]) - numbers[4]) == 1 and len(j) == 6:
                numbers[9] = set(j)
            elif len((set(j) - numbers[7]) - numbers[4]) == 1 and len(j) == 5:
                numbers[5] = set(j)
            elif len(j) == 6:
                numbers[6] = set(j)
            elif len(j) == 5:
                numbers[2] = set(j)
        numb = ''
        for e in i[1]:
            for j in range(10):
                if set(e) == numbers[j]:
                    numb += str(j)
                    break
        summa += int(numb)
        print(summa)


if __name__ == '__main__':
    main()

