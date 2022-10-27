from time import perf_counter
import numpy as np
if __name__ == '__main__':
    start = perf_counter()
    pas = 'cqjxjnds'
    invalid = 0

    def incr(pa):
        return 'a' + incr(pa[1:]) if (ord(pa[0])+1) > ord('z') else chr(ord(pa[0])+1) + pa[1:]

    while invalid != 2:
        pas = incr(pas[::-1])[::-1]
        dub = 0
        seq = 0
        if 'i' not in pas and 'l' not in pas and 'o' not in pas:
            prev = ''
            count = 0
            dubc = ''
            for i in pas:
                if prev and ord(prev)+1 == ord(i):
                    count += 1 
                else:
                    count = 0
                seq = 1 if count == 2 else seq
                if prev and prev == i:
                    if dubc and i != dubc:
                        dub = 1
                    else:
                        dubc = i
                prev = i
        if dub and seq:
            invalid += 1
    b = perf_counter()
    print(b-start)
    print(pas)
                
                

