import itertools
from time import sleep

class Tetris:
    def __init__(self, type) -> None:
        match type:
            case 'flat': self.shape = [2,3,4,5]
            case '+': self.shape = [2+1j,3+1j,4+1j,3+2j,3]
            case 'L': self.shape = [2,3,4,4+1j,4+2j]
            case 'long': self.shape = [2,2+1j,2+2j,2+3j]
            case 'square': self.shape = [2,3,2+1j,3+1j]
        self.shape = [i+(highest+4)*1j for i in self.shape]

    def move(self, direction):
        global cave
        if direction=='<':
            if 0 not in [int(i.real) for i in self.shape]:
                shape = set([i-1 for i in self.shape])
                if shape&cave==set():
                    self.shape = [i-1 for i in self.shape]
        elif direction=='>':
            if 6 not in [int(i.real) for i in self.shape]:
                shape = set([i+1 for i in self.shape])
                if shape&cave==set(): self.shape = shape
        
    def down(self):
        global cave, highest
        shape = set([i-1j for i in self.shape])
        if shape&cave==set():
            self.shape = [i-1j for i in self.shape]
            return 0
        else:
            cave.update(self.shape)
            self.top = max([int(i.imag) for i in self.shape])
            return 1
        
def visualize():
    for i in range(30,-1,-1):
        for j in range(7):
            if j+1j*i in cave:
                print('#', end='')
            elif j+1j*i in current.shape:
                print('@', end='')
            else:
                print('.', end='')
        print()

def run(n,visual=False):
    global cave, current, highest
    with open(r'2022\17\input.txt', 'r') as openfile:
        data = openfile.read().strip()
    stream = itertools.cycle(data)
    highest, cnt = -1, 0
    cave = set([i-1j for i in range(1,8)])
    order = ['flat', '+', 'L', 'long', 'square']
    stream_len = len(data)
    diffs, heights = {}, []
    for k in range(n):
        current = Tetris(order[k%5])
        for j in stream:
            cnt += 1
            if cnt%stream_len==0:
                for i in heights:
                    di = highest-i
                    if di in diffs:
                        return (n//(k-diffs[di]))*(di)  + run(n%(k-diffs[di]))
                    else:
                        diffs[highest-heights[0]] = k
                heights.append(highest)
            if visual:
                sleep(0.5)
                visualize()
                print()
            current.move(j)
            if current.down():
                highest = max(current.top,highest)
                break
    return highest+1

def main():
    print('Part 1:',run(2022))
    print('Part 2:',run(1000000000000))
    run(15,visual=True)

if __name__ == '__main__':
    main()
