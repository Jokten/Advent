class Node:
    def __init__(self,val):
        self.next = None
        self.val = val

    def add_next(self,next):
        self.next = next
        return next

def list_creator(str):
    k = 0
    for i in str:
        ny = Node(i)
        if k == 0:
            star = ny
            nod = ny
            k = 1
        else:
            nod.add_next(ny)
            nod = ny
    return star

def main():
    with open('input.txt', 'r') as file:
        start = file.readline()
        next(file)
        rule = [i.split(' -> ') for i in file.read().splitlines()]
    rule_book = {i[0]:i[1] for i in rule}
    link = list_creator(start)
    first = link
    for i in range(40):
        print(i)
        link = first
        while link.next != None:
            next_node = link.next
            if (link.val + next_node.val) in rule_book:
                new = Node(rule_book[link.val+next_node.val])
                link.add_next(new)
                new.add_next(next_node)
            link = next_node
    skriv = first
    freq = {}
    while skriv.next != None:
        if skriv.val in freq:
            freq[skriv.val] += 1
        else:
            freq[skriv.val] = 1
        skriv = skriv.next
    print(sorted(freq.values()))
if __name__ == '__main__':
    main()
