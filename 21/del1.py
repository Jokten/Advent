def create_die():
    n = 0
    while True:
        n = (n%100)+1
        yield n


def roll_die(die):
    return next(die) + next(die) + next(die)


def main():
    die = create_die()
    points = [0, 0]
    positions = [3, 9]
    rolls = 0
    while points[0] < 1000 and points[1] < 1000:
        print(points)
        for i in range(2):
            positions[i] = (positions[i]+roll_die(die))%10
            rolls += 3
            points[i] += positions[i] + 1
            if points[i] > 1000:
                score = rolls * points[not i]
                return score


if __name__ == '__main__':
    print(main())