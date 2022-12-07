import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)).split('2022')[0])
import aoctools

class terminal:
    def __init__(self):
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
    
    def count(self):
        self.cd('/')
        self.left = 70000000 - self._count(self.dirs)
        return 1
    
    def _count(self, dirs):
        sum = 0
        for i in dirs.keys():
            if type(dirs[i]) == int: sum += dirs[i]
            else: sum += self._count(dirs[i])
        self.dir_sizes.append(sum)
        return sum
    
    def delete(self, size):
        return min([i for i in self.dir_sizes if self.left+i > size])

def main():
    data = aoctools.data_loader(2022, 7, two_parts=False)
    term = terminal()
    for k in data:
        match k.split():
            case '$', 'cd', x: term.cd(x)
            case '$', 'ls': pass
            case 'dir', x: term.dirs.setdefault(x,{})
            case size, name: term.dirs.setdefault(name, int(size))
    term.count()
    print(sum([i for i in term.dir_sizes if i < 100000]))
    print(min([i for i in term.dir_sizes if term.left+i > 30000000]))
if __name__ == "__main__":
    main()