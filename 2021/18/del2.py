import math


class Tree:
    def __init__(self, depth, array, root, pos):
        self.depth = depth
        self.pos = pos
        self.branch = []
        self.root = root
        for e, i in enumerate(array):
            if type(i) is list:
                self.branch.append(Tree(depth + 1, i, self, e))
            else:
                self.branch.append(i)

    def explode(self):
        if self.depth == 4:
            sv = self.branch
            for e, i in enumerate(self.branch):
                self.root.send_down(i, e, self.pos)
            self.root.branch[self.pos] = 0
        for e, i in enumerate(self.branch):
            if isinstance(i, Tree):
                i.explode()

    def split(self):
        for e, i in enumerate(self.branch):
            if isinstance(i, int) and i > 9:
                self.branch[e] = Tree(self.depth + 1, [math.floor(i / 2), math.ceil(i / 2)], self, e)
                return True
            elif isinstance(i, Tree):
                if i.split():
                    return True

    def send_up(self, pack, adress):
        if isinstance(self.branch[adress], int):
            self.branch[adress] += pack
        else:
            self.branch[adress].send_up(pack, adress)

    def send_down(self, pack, adress, position):
        if isinstance(self.branch[adress], int):
            self.branch[adress] += pack
        elif adress != position:
            self.branch[adress].send_up(pack, not adress)
        elif self.root is not None:
            self.root.send_down(pack, adress, self.pos)

    def magnitude(self):
        val = [0, 0]
        for i in range(2):
            if isinstance(self.branch[i],int):
                val[i] = self.branch[i]
            else:
                val[i] = self.branch[i].magnitude()

        return 3*val[0] + 2*val[1]

    def __str__(self):
        return f'[{str(self.branch[0])},{str(self.branch[1])}]'


def main():
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
    combinations = []
    maxmagn = 0
    for i in data:
        for j in data:
            combinations.append(f'[{i},{j}]')
    for i in combinations:
        snail = eval(i)
        snail_tree = Tree(0, snail, None, None)
        old = ''
        while old != str(snail_tree):
            old = str(snail_tree)
            snail_tree.explode()
            snail_tree.split()
        magn = snail_tree.magnitude()
        if magn > maxmagn:
            maxmagn = magn
    print(maxmagn)


if __name__ == '__main__':
    main()
