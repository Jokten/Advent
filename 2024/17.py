import aoc, re

def run(program, A):
    out, sp = [], 0
    regs = [0, 1, 2, 3, A, 0, 0]
    while sp < len(program):
        op, val = program[sp], program[sp+1]
        match op:
            case 0: regs[4] >>= regs[val]
            case 1: regs[5] ^= val
            case 2: regs[5] = regs[val]&7
            case 3: sp = val-2 if regs[4] != 0 else sp
            case 4: regs[5] ^= regs[6]
            case 5: out.append(regs[val]&7)
            case 6: regs[5] = regs[4]>>regs[val]
            case 7: regs[6] = regs[4]>>regs[val]
        sp += 2
    return out

def findA(prog, A,ind):
    A <<= 3
    for i in range(8):
        if run(prog, A|i)[0] == prog[-ind-1]:
            if ind == len(prog)-1: return A|i
            r = findA(prog,A|i, ind+1)
            if r != -1: return r
    return -1

data = aoc.get_data(2024,17).split("\n")

A = int(re.findall(r"\d+",data[0])[0])
program = [int(i) for i in (re.findall(r"\d",data[-1]))]
print(run(program,A),findA(program, 0, 0))
