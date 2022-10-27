import numpy as np
if __name__ == '__main__':
    with open('day8\input.txt') as file:
        data = file.read().splitlines()
    chars = 0
    code = 0
    for i in data:
        print(len(i))
        chars += len(i)
        #code += len(eval(i))
        code += len(i) + i.count("\"") + i.count("\\") +2
    print(chars-code)