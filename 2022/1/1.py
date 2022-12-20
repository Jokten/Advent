with open('2022/1/input.txt') as f: elfs = sorted([sum(map(int, i.split('\n'))) for i in f.read().split('\n\n')])
print(elfs[0], sum(elfs[-3:]))