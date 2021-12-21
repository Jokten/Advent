

def roll_dice(turn, points, position, universe, dice_roll):
    points = points.copy()
    position = position.copy()

    universe *= dice_roll[0]
    position[turn] = (position[turn] + dice_roll[0])%10
    points[turn] += position[turn] + 1
    if points[turn] >= 21:
        total_universe[turn] += universe
    else:
        for i in possible:
            roll_dice(not turn, points, position, universe, i)



def main():
    global possible
    possible = ((1, 3), (3, 4), (6, 5), (7, 6), (6, 7), (3, 8), (1, 9))
    global total_universe
    total_universe = [0, 0]
    universe = 1
    positions = [4, 10]
    points = [0, 0]
    for i in possible:
        roll_dice(0, points, positions, universe, i)
    print(total_universe)




if __name__ == '__main__':
    print(main())