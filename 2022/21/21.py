import re
import time
import z3

monkeys = {}
with open(r'2022\21\input.txt', 'r') as openfile:
    data = openfile.read().splitlines()
    data = [i.split(' ') for i in data]
non = set()
for i in data:
    if i[1].isnumeric():
        monkeys[i[0][:-1]] = int(i[1])
    else:
        non.add((i[0][:-1], i[1], i[2], i[3]))
root = 1
org = monkeys.copy()
seto = non.copy()

MAX = 9999999999999999
MIN = 0
while root:
    non = seto.copy()
    monkeys = org.copy()
    current = (MAX+MIN)//2
    monkeys['humn'] = current
    while non:
        new_non = non.copy()
        for i in non:
            if i[1] in monkeys and i[3] in monkeys:
                if i[0] == 'root':
                    diff = (monkeys[i[1]]- monkeys[i[3]])
                    if diff == 0:
                        root = 0
                        print(current)
                if i[2] == '/':
                    monkeys[i[0]] = monkeys[i[1]] // monkeys[i[3]]
                else:
                    monkeys[i[0]] = eval(str(monkeys[i[1]]) + str(i[2]) + str(monkeys[i[3]]))
                new_non.remove(i)
        non = new_non
    print(current, diff)
    if diff > 0:
        MIN = current
    else:
        MAX = current