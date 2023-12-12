import math

def main():
    with open(r".\2023\8\input.txt") as f:
        lines = f.read()
    lines = lines.split('\n\n')
    inst = lines[0]
    maps = lines[1].splitlines()
    maps = [i.split(' = ') for i in maps]
    mapp = {}
    for i in maps:
        mapp[i[0]] = (i[1][1:4],i[1][6:-1])
    curr = 'AAA'
    steps = 0
    while curr != 'ZZZ':
        i = inst[steps%len(inst)]
        if i == 'R':
            curr = mapp[curr][1]
        elif i == 'L':
            curr = mapp[curr][0]
        steps += 1
    print(f'Part 1: {steps}')

    starter = []
    for i in mapp.keys():
        if i[-1] == 'A':
            starter.append(i)
    totsteps = []
    steps = 0
    while starter:
        remove = []
        for e,i  in enumerate(starter):
            if i[-1] == 'Z':
                totsteps.append(steps)
                remove.append(e)
            else:
                ins = inst[steps%len(inst)]
                if ins == 'R':
                    starter[e] = mapp[i][1]
                elif ins == 'L':
                    starter[e] = mapp[i][0]
        for i in sorted(remove,reverse=True): del starter[i]
        steps += 1
    ans = math.lcm(*totsteps)
    print(f'Part 2: {ans}')

if __name__ == "__main__":
    main()