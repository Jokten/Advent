import numpy as np
def time_increase(squid):
    for i in range(len(squid)):
        for j in range(len(squid)):
            squid[i][j] += 1


def flash_increase(squid, point):
    ymax = min(point[1]+2, len(squid))
    xmax = min(point[0]+2, len(squid))
    ymin = max(point[1]-1, 0)
    xmin = max(point[0] - 1, 0)
    squid[xmin:xmax, ymin:ymax] += 1
    squid[point[0], point[1]] = -100

def main():
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
    squid = np.array([[int(j) for j in i] for i in data])
    flash_counter = 0
    time = 0
    while flash_counter != (len(squid))**2:
        flash_counter = 0
        time_increase(squid)
        time += 1
        flash = 1
        while flash == 1:
            flash = 0
            for i in range(len(squid)):
                for j in range(len(squid)):
                    if squid[i][j] > 9:
                        flash_increase(squid, [i, j])
                        flash_counter += 1
                        flash = 1
        squid[squid < 0] = 0
    print(flash_counter)
    print(squid)
    print(time)
if __name__ == '__main__':
    main()