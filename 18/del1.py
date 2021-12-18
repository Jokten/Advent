import math


class Tree:
    def __init__(self, depth, array, root):
        self.depth = depth
        self.branch = []
        self.root = root
        for e, i in enumerate(array):
            if type(i) is list:
                self.branch.append(Tree(depth + 1, i, self))
            else:
                self.branch.append(i)

    def reduce(self):
        print(self.depth)
        for e, b in enumerate(self.branch):

            if isinstance(b, Tree) and b.depth >= 4:
                print('geh')
                sv = b.branch
                self.branch[e] = 0
                val = not e
                if self.branch[val] is int:
                    self.branch[val] += sv[val]
                    sv[val] = 0
                self.root.send_down(sv, e)

            elif type(b) is int and b > 9:
                arr = [math.ceil(b), math.floor(b)]
                self.branch[e] = Tree(self.depth + 1, arr, b)
                self.branch[e].reduce()
            elif isinstance(b, Tree):
                b.reduce()

    def send_down(self, pack, orientation):

        if isinstance(self.branch[0], int):
            self.branch[0] += pack[0]
        else:
            uppack1 = pack.copy()
            uppack1[orientation] = 0
            self.branch[orientation].send_up(uppack1)
        if isinstance(self.branch[1], int):
            self.branch[1] += pack[1]
        else:
            uppack2 = pack.copy()
            uppack2[not orientation] = 0
            self.branch[not orientation].send_up(uppack2)
        print(self.root)
        if self.root is not None:
            print(self.root)
            self.root.send_down(pack, orientation)

    def send_up(self, pack):
        for e, b in enumerate(self.branch):
            if type(b) is int:
                self.branch[e] += pack[e]
                pack[e] = 0
            else:
                nextpack = pack.copy()
                nextpack[not e] = 0
                b.send_up(nextpack)

    def __str__(self):
        return f'[{str(self.branch[0])},{str(self.branch[1])}]'


def main():
    # with open('input.txt', 'r') as file:
    #    data = file.read().splitlines()
    line = '[[[[[9,8],1],2],3],4]'
    snail = eval(line)
    snail_tree = Tree(0, snail, None)
    snail_tree.reduce()
    print(snail_tree)


if __name__ == '__main__':
    main()
