import itertools
import numpy as np
    
def find_all_factors(n):
    # Find all factors of n
    factors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            factors.append(i)
            if n//i != i:
                factors.append(n//i)
    return factors


if __name__ == '__main__':
    inp = 34000000
    total = 0
    count = 0
    while total < inp:
        count += 1
        total = sum([i for i in find_all_factors(count) if count//i < 51])*11
    print(count)
