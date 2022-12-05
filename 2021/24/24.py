

def load_data():
    with open("2021\\24\\input.txt", "r") as f:
        data = f.read().splitlines()
    return data

def execute(inst,z,w):
    reg = {'x':0, 'y':0, 'z':z, 'w':w}
    for i in inst[1:]:
        if i[0] == 'add': reg[i[1]] += (reg[i[2]] if i[2].isalpha() else int(i[2]))
        elif i[0] == 'mul': reg[i[1]] *= (reg[i[2]] if i[2].isalpha() else int(i[2])) 
        elif i[0] == 'div': reg[i[1]] //= (reg[i[2]] if i[2].isalpha() else int(i[2]))
        elif i[0] == 'mod': reg[i[1]] %= (reg[i[2]] if i[2].isalpha() else int(i[2]))
        elif i[0] == 'eql': reg[i[1]] = reg[i[1]] == (reg[i[2]] if i[2].isalpha() else int(i[2]))
    return reg['z']

def split_mods(data):
    sections = []
    sect = ['inp w']
    for i in range(1,len(data)):
        if data[i][0] == 'inp':
            sections.append(sect)
            sect = []
        sect.append(data[i])
    sections.append(sect)
    return sections

def solver(ins,out):
    possibles = []
    for z in range(26):
        for w in range(10):
            if execute(ins[0],z,w) == out: possibles.append((z,w))
    answ = []
    if len(ins) == 1: return possibles
    for i in possibles:
        answ.append(str(i[1])+solver(ins[1:],i[0]))
    return str(max([int(i) for i in answ]))


def main():
    
    d = [i.split(' ') for i in load_data()]
    lis = split_mods(d)
    lis.reverse()
    print(lis)
    print(len(lis))
    vals = []
    for i in lis:
        possibles = []
        out = 1
        for w in range(10):
            for z in range(2600):
                output = execute(i,z,w)
                if output == 26: possibles.append((z,w))
        print(possibles)



if __name__ == "__main__":
    main()
