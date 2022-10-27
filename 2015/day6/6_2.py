import numpy as np
if __name__ == '__main__':
    with open('day6\input.txt') as file:
        data = file.read().splitlines()
    lights = np.zeros((1000,1000))
    for instructions in data:
        i = list(filter(lambda x: x not in ['turn', 'through'],instructions.split()))
        startx, starty = tuple(map(int,i[1].split(',')))
        endx, endy = tuple(map(int,i[2].split(',')))

        if i[0] == 'on':
            lights[startx:endx+1,starty:endy+1] += 1
        elif i[0] == 'off':
            lights[startx:endx+1,starty:endy+1] -= 1
            lights[lights<0] = 0
        else:
            lights[startx:endx+1,starty:endy+1] += 2
    print(sum(sum(lights)))
    x = np.array([1,0,1,1,0])
    print(x[:] == 0)