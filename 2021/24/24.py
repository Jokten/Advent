

def load_data():
    with open("2021\\24\\input.txt", "r") as f:
        data = f.read().splitlines()
    return data

def execute(inst, z, w):
    # 1 or 26
    x = (z%26) + inst[1]
    z = z//inst[0]

    if x!=w:
        z *= 26
        z += w + inst[2]
    
    return z
    

def split_mods(data):
    sections = []
    sect = [['inp', 'w']]
    for i in range(1,len(data)):
        if data[i][0] == 'inp':
            sections.append(sect)
            sect = []
        sect.append(data[i])
    sections.append(sect)
    return sections



def main(): 
    d = [i.split(' ') for i in load_data()]
    lis = split_mods(d)

    instructions = []
    intresting = [4, 5, 15]
    for k in intresting:
        inst = []
        for i in lis:
            inst.append(i[k])
        instructions.append(inst)
    
    reduced_instructions = []
    for i in range(len(instructions[0])):
        reduced_instructions.append((int(instructions[0][i][2]), int(instructions[1][i][2]), int(instructions[2][i][2])))

    # reduced_instructions.reverse()
    print(reduced_instructions)
    w = [9 for i in range(len(reduced_instructions))]
    z = []
    for i in reduced_instructions:
        if i[0] == 26:

    s = ''
    for i in w:
        s += '9'
    print(s)

    
    
    

            
    

if __name__ == "__main__":
    main()
