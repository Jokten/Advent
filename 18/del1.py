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
            #print(f'Explosion {sv}')
            for e, i in enumerate(self.branch):
                self.root.send_down(i, e, self.pos)
                #print(f'Sent {i} with adress {e} to {self.root}')
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
            #print(type(self.branch[adress]),type(pack))
            self.branch[adress] += pack
        else:
            self.branch[adress].send_up(pack, adress)

    def send_down(self, pack, adress, position):
        if isinstance(self.branch[adress], int):
            self.branch[adress] += pack
        elif adress != position:
            self.branch[adress].send_up(pack, not adress)
        elif self.root is not None:
            #print(f'Sent {pack} with adress {adress} to {self.root}')
            self.root.send_down(pack, adress, self.pos)

    def magnitude(self):
        if isinstance(self.branch[0],int):
            val1 = self.branch[0]
        else:
            val1 = self.branch[0].magnitude()
        if isinstance(self.branch[1],int):
            val2 = self.branch[1]
        else:
            val2 = self.branch[1].magnitude()

        return 3*val1 + 2*val2

    def __str__(self):
        return f'[{str(self.branch[0])},{str(self.branch[1])}]'


def main():
    with open('input.txt', 'r') as file:
        first = next(file)
        data = file.read().splitlines()
    snail = eval(first)
    snail_tree = Tree(0, snail, None, None)
    old = ''
    while old != str(snail_tree):
        old = str(snail_tree)
        print(old)
        snail_tree.explode()
        snail_tree.split()
    print(old)
    for i in data:
        new_arr = eval(f'[{str(snail_tree)},{i}]')
        snail_tree = Tree(0, new_arr, None, None)
        old = ''
        while old != str(snail_tree):
            old = str(snail_tree)
            print(old)
            snail_tree.explode()
            snail_tree.split()
    print(snail_tree.magnitude())
    print(snail_tree)


if __name__ == '__main__':
    main()
