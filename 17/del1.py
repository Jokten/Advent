def findy(border,side):
    tot = 0
    for j in range(side[1]+5):
        for i in range(border[0],102):
            ypos = 0
            xpos = 0
            vx = j
            vy = i

            while ypos > border[0]:
                xpos += vx
                ypos += vy
                vx = max([vx-1,0])
                vy -= 1
                if border[1] >= ypos >= border[0] and side[1] >= xpos >= side[0]:
                    tot += 1
                    break
    return tot



def main():
    #with open('input.txt', 'r') as file:
    #    data = file.read()
    data = (-102,-78),(135,155)
    testdata = ((-10,-5),(20,30))
    print(findy(data[0],data[1]))


if __name__ == '__main__':
    main()
