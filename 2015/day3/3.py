if __name__ == '__main__':
    with open('day3\input.txt') as file:
        places = set()
        startx = 0
        starty = 0
        places.add((0,0))
        data = list(file.read())
        data_santa = data[::2]
        data_robo = data[1::2]
        for i in data_santa:
            if i=='^':
                starty += 1
            elif i=='v':
                starty -= 1
            elif i=='<':
                startx -= 1
            elif i=='>':
                startx += 1
            else:
                print('fel')
            places.add((startx, starty))
        startx = 0
        starty = 0
        for i in data_robo:
            if i=='^':
                starty += 1
            elif i=='v':
                starty -= 1
            elif i=='<':
                startx -= 1
            elif i=='>':
                startx += 1
            else:
                print('fel')
            places.add((startx, starty))
        print(len(places))