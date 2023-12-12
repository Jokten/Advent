import re

def main():
    with open(r".\2023\2\input.txt", "r") as f:
        lines = f.readlines()
        
    lines = [line.strip().replace(";",',') for line in lines]

    lines = [[i.strip().split(" ") for i in line.split(",")] for line in lines]
    print(lines)
    sum = 0
    for line in lines:
        id = int(line[0][1][:-1])
        di= {'red':0, 'green':0, 'blue':0}
        for i in line:
            if len(i) == 4:
                if int(i[2]) > di[i[3]]:
                    di[i[3]] = int(i[2])
            else:
                if int(i[0]) > di[i[1]]:
                    di[i[1]] = int(i[0])
        # else:
        #     sum += id
        m = 1
        for i in di.values():
            m *= i
        sum += m
    print(sum)


        
if __name__ == "__main__":
    main()