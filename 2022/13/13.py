from functools import cmp_to_key

def comp(x, y):
    if isinstance(x, int) and isinstance(y, int):
        if x > y: return -1
        if x < y: return 1
        return 0
    if isinstance(x, int): x = [x]
    if isinstance(y, int): y = [y]
    for item in list(zip(x, y)):
        val = comp(item[0], item[1])
        if val != 0: return val
    if len(x) > len(y): return -1
    if len(x) < len(y): return 1
    return 0
        
def main():
    with open(r'2022\13\input.txt', 'r') as file:
        data = file.read().split('\n\n')
    data = [[eval(j) for j in i.split('\n')] for i in data]
    
    # part 1
    print(f'Part 1: {sum([e for e,i in enumerate(data,1) if comp(i[0], i[1]) == 1])}')

    # part 2
    lis = [i for i in [j for j in data]]
    lis = [item for sublist in data for item in sublist] + [[[2]],[[6]]]
    lis = sorted(lis, key=cmp_to_key(comp), reverse=True)
    print(f'Part 2: {(lis.index([[2]])+1) * (lis.index([[6]])+1)}')
        
if __name__ == '__main__':
    main()