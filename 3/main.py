def most_common(lista, n):
    one = 0
    zero = 0
    for i in lista:
        if i[n] == '1':
            one += 1
        else:
            zero += 1
    if one >= zero:
        return '1'
    else:
        return '0'


def main():
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
    gamma_str = ''
    for i in range(len(data[0])):
        gamma_str += most_common(data, i)
    gamma = int(gamma_str, 2)
    epsilon = 2**(len(data[0]))-1-gamma
    print(gamma*epsilon)

if __name__ == '__main__':
    main()