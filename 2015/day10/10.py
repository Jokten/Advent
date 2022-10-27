
import numpy as np
if __name__ == '__main__':
    s = '1321131112'
    next = []
    for i in range(50):
        new_s = []
        prev = s[0]
        count = 1
        for j in s[1:]:
            if j != prev:
                new_s += [str(count), prev]
                count = 1
            else:
                count += 1
            prev = j
        new_s += [str(count), prev]
        s = "".join(new_s)
    print(len(s))
