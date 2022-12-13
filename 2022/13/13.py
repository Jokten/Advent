from functools import cmp_to_key

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a > b: return -1
        if a < b: return 1
        return 0
    if isinstance(a, int): x = [a]
    if isinstance(b, int): y = [b]
    if isinstance(a, list): x = a
    if isinstance(b, list): y = b
    items = list(zip(x, y))
    for item in items:
        val = compare(item[0], item[1])
        if val != 0: return val
    if len(x) > len(y): return -1
    if len(x) < len(y): return 1
    return 0
        
def main():
    with open(r'2022\13\input.txt', 'r') as file:
        data = file.read()
    data = data.split('\n\n')
    data = [i.split('\n') for i in data]
    data = [[eval(j) for j in i] for i in data]
    
    # part 1
    sum = 0
    for e,i in enumerate(data):
        if compare(i[0], i[1]) == 1:
            sum += e+1
    print(f'Part 1: {sum}')

    # part 2
    lis = []
    for i in data: lis += [i[0], i[1]]
    lis += [[[2]],[[6]]]
    lis = sorted(lis, key=cmp_to_key(compare), reverse=True)
    s = (lis.index([[2]])+1) * (lis.index([[6]])+1)
    print(f'Part 2: {s}')
        
if __name__ == '__main__':
    main()