import numpy as np

def cycle(data):

    for i in range(4):
        old = ''
        cur = ''.join([''.join(i) for i in data])
        while old != cur:
            old = cur
            for i in range(len(data[0])):
                for j in range(1,len(data)):
                    if data[j][i] == 'O' and data[j-1][i] == '.':
                        data[j][i] = '.'
                        data[j-1][i] = 'O'
            cur = ''.join([''.join(i) for i in data])

        data = [[i[j] for i in data[::-1]] for j in range(len(data[0]))]

    row = len(data)
    sum = 0
    for i in data:
        sum += i.count('O') * row
        row -= 1
    return sum, data

def main():
    with open('2023/14/input.txt') as f: data = f.readlines()
    data = [list(i.strip()) for i in data]
    cyc = set()
    cycdet = 0
    cnt = 0
    while True:
        cnt += 1
        sum, data = cycle(data)
        st = ''.join([''.join(i) for i in data])
        if st in cyc:
            cy = [sum]
            while True:
                s2, data = cycle(data)
                if s2 == sum: break
                else: cy.append(s2)
            break
        else: cyc.add(st)
    
    while True:
        s2, data = cycle(data)
        if s2 == sum:
            break
        else:
            cy.append(s2)

    print(cy[(1000000000 - cnt) % len(cy)])

            
    
            

        

if __name__ == '__main__':
    main()