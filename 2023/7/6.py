import time
from functools import cache, cmp_to_key

def high(a,b, joke = False):
    if joke:
        order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4','3', '2', 'J']
    else:
        order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4','3', '2']
    order.reverse()
    for i in range(5):
        if order.index(a[i]) > order.index(b[i]): return 1
        elif order.index(a[i]) < order.index(b[i]): return -1
    return 0

def card_count(a, joke = False):
    if joke:
        order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4','3', '2', 'J']
    else:
        order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4','3', '2']
    counts = [0 for i in range(13)]
    for i in a:
        counts[order.index(i)] += 1
    return counts

@cache
def comp(aa, bb, joke = False):
    a, b = list(aa), list(bb) 
    if joke:
        while 'J' in a or 'J' in b:
            if 'J' in a: a.remove('J')
            if 'J' in b: b.remove('J')
    la, lb = len(a), len(b)
    ac, bc = card_count(a, joke), card_count(b, joke)

    if max(len(set(a)),1) > max(len(set(b)),1):
        return -1
    elif max(len(set(a)),1) < max(len(set(b)),1):
        return 1
    else:
        if max(len(set(a)),1) == 1:
            return high(aa,bb, joke)
        
        elif len(set(a)) == 2:
            if la-1 in ac: return high(aa,bb, joke) if lb-1 in bc else 1
            else: return -1 if lb-1 in bc else high(aa,bb, joke)

        elif len(set(a)) == 3:
            if la-2 in ac: return high(aa,bb, joke) if lb-2 in bc else 1
            else: return -1 if lb-2 in bc else high(aa,bb, joke)

        elif len(set(a)) == 4:
            return high(aa,bb, joke)
        if len(set(a)) == 5:
            return high(aa,bb, joke)


def main():
    p2 = True
    with open(r".\2023\7\input.txt") as f:
        lines = f.readlines()
    lines = [line.split() for line in lines]
    lines.sort(key=cmp_to_key(lambda x, y: comp(x[0], y[0], p2)))
    score = sum([(e+1)*int(i[1]) for e,i in enumerate(lines)])

    print(score)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
