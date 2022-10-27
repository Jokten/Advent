import numpy as np
if __name__ == '__main__':
    with open('day5\input.txt') as file:
        data = file.read().splitlines()
    nice = 0
    for word in data:
        double = 0
        spaced = 0
        for i in range(len(word)-1):
            if len(word.split(word[i]+word[i+1]))>2: 
                double = 1
        for i in range(2,len(word)):
            if word[i-2] == word[i]:
                spaced = 1
        if spaced == 1 and double == 1:
            nice += 1
    print(nice)
    print(len(data))