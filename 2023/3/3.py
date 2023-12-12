import re


def main():
    with open(r".\2023\3\input.txt") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    i = 0

    sum = 0
    while i < len(lines):
        j = 0
        while j < len(lines[i]):
            print(i,j)
            if lines[i][j].isnumeric():
                num = ""
                valid = False
                while j < len(lines[i]) and i < len(lines) and lines[i][j].isnumeric():
                    num += lines[i][j]
                    lowi = max(1,i-1)
                    lowj = max(1,j-1)
                    highi = min(len(lines)-1,i+1)
                    highj = min(len(lines[i])-1,j+1)
                    if lines[lowi][lowj] != ".":
                        if not lines[lowi][lowj].isnumeric():
                            valid = True
                    if lines[lowi][j] != ".":
                        if not lines[lowi][j].isnumeric():
                            valid = True
                    if lines[lowi][highj] != ".":
                        if not lines[lowi][highj].isnumeric():
                            valid = True
                    if lines[i][lowj] != ".":
                        if not lines[i][lowj].isnumeric():
                            valid = True
                    if lines[i][highj] != ".":
                        if not lines[i][highj].isnumeric():
                            valid = True
                    if lines[highi][lowj] != ".":
                        if not lines[highi][lowj].isnumeric():
                            valid = True
                    if lines[highi][j] != ".":
                        if not lines[highi][j].isnumeric():
                            valid = True
                    if lines[highi][highj] != ".":
                        if not lines[highi][highj].isnumeric():
                            valid = True

                    j += 1
                if valid:
                    sum += int(num)
            j += 1
        i += 1
    print(sum)
            

def p2():
                    
    with open(r".\2023\3\input.txt") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    i = 0
    gears = {}
    sum = 0
    print(len(lines))
    print(len(lines[0]))
    while i < len(lines):
        j = 0
        while j < len(lines[i]):
            print(i,j)
            if lines[i][j].isnumeric():
                num = ""
                valids = set()
                while j < len(lines[i]) and i < len(lines) and lines[i][j].isnumeric():
                    num += lines[i][j]
                    lowi = max(1,i-1)
                    lowj = max(1,j-1)
                    highi = min(len(lines)-1,i+1)
                    highj = min(len(lines[i])-1,j+1)
                    
                    if lines[lowi][lowj] == "*":
                        valids.add((lowi,lowj))
                    if lines[lowi][j] == "*":
                        valids.add((lowi,j))
                    if lines[lowi][highj] == "*":
                        valids.add((lowi,highj))
                    if lines[i][lowj] == "*":
                        valids.add((i,lowj))
                    if lines[i][highj] == "*":
                        valids.add((i,highj))
                    if lines[highi][lowj] == "*":
                        valids.add((highi,lowj))
                    if lines[highi][j] == "*":
                        valids.add((highi,j))
                    if lines[highi][highj] == "*":
                        valids.add((highi,highj))
                    j += 1
                    print(valids)
                for valid in valids:
                    if valid not in gears:
                        gears[valid] = [int(num)]
                    elif num not in gears[valid]:
                        gears[valid].append(int(num))
            j += 1
        i += 1
    print(gears)
    for gear in gears.values():

        if len(gear) == 2:
            sum += gear[0] * gear[1]
    print(sum)
        
if __name__ == "__main__":
    p2()