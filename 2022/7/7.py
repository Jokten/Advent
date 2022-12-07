import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)).split('2022')[0])
import aoctools

class terminal():
    def __init__(self):
        self.sum = 0
        self.dirs = {}
        self.parent = []
        self.outer = self.dirs
        self.dir_sizes = []

    def cd(self, path):
        if path == '..':
            self.dirs = self.parent.pop()
        elif path == '/':
            self.dirs = self.outer
            self.parent = []
        else:
            self.parent.append(self.dirs)
            self.dirs = self.dirs[path]
    
    def dir(self, name):
        if name not in self.dirs.keys():
            self.dirs[name] = {}

    def add(self, name, value):
        self.dirs[name] = value

    def count(self):
        sum = 0
        self.cd('/')
        for i in self.dirs.keys():
            if type(self.dirs[i]) == int:
                sum += self.dirs[i]
            else:
                sum += self._count(self.dirs[i])
        if sum < 100000:
            self.sum += sum
        self.left = 70000000 - sum
        return self.sum
    
    def _count(self, dirs):
        sum = 0
        for i in dirs.keys():
            if type(dirs[i]) == int:
                sum += dirs[i]
            else:
                sum += self._count(dirs[i])
        if sum < 100000:
            self.sum += sum
        self.dir_sizes.append(sum)
        return sum
    
    def delete(self, size):
        return min([i for i in self.dir_sizes if self.left+i > size])

def main():
    data = aoctools.data_loader(2022, 7, two_parts=False)
    term = terminal()
    for k in data:
        i = k.split(' ')
        if i[0] == '$':
            if i[1] == 'cd':
                term.cd(i[2])
            elif i[1] == 'ls':
                pass
        elif i[0] == 'dir':
            term.dir(i[1])
        else:
            term.add(i[1], int(i[0]))
    print(term.count())
    print(term.delete(30000000))


if __name__ == "__main__":
    main()