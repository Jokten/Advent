import numpy as np
if __name__ == '__main__':
    with open('day7\input.txt') as file:
        data = file.read().splitlines()
    ins = [line.split() for line in data]
    fail_ins = []
    wires = {'b':3176}
    while ins:
        for i in ins:
            if len(i) == 3 and i[2] == 'b':
                continue
            if 'NOT' in i and i[1] in wires.keys():
                wires[i[3]] = 2^16-1-wires[i[1]]
            elif 'AND' in i:
                if i[0] in wires.keys() and i[2] in wires.keys():
                    wires[i[4]] = wires[i[0]] & wires[i[2]]
                elif i[0].isnumeric() and i[2] in wires.keys():
                    wires[i[4]] = int(i[0]) & wires[i[2]]
                else:
                    fail_ins.append(i)
            elif 'OR' in i and i[0] in wires.keys() and i[2] in wires.keys():
                wires[i[4]] = wires[i[0]] | wires[i[2]]
            elif 'LSHIFT' in i:
                if i[0] in wires.keys() and i[2] in wires.keys():
                        wires[i[4]] = wires[i[0]] << wires[i[2]]
                elif i[2].isnumeric() and i[0] in wires.keys():
                    wires[i[4]] = wires[i[0]] << int(i[2])
                else:
                    fail_ins.append(i)
            elif 'RSHIFT' in i:
                if i[0] in wires.keys() and i[2] in wires.keys():
                        wires[i[4]] = wires[i[0]] >> wires[i[2]]
                elif i[2].isnumeric() and i[0] in wires.keys():
                    wires[i[4]] = wires[i[0]] >> int(i[2])
                else:
                    fail_ins.append(i)
            elif len(i) == 3:
                if i[0].isnumeric():
                    wires[i[2]] = int(i[0])
                elif i[0] in wires.keys():
                    wires[i[2]] = wires[i[0]]
                else:
                    fail_ins.append(i)
            else:
                fail_ins.append(i)
        ins = fail_ins
        fail_ins = []
    print(wires['a'])