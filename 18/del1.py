def _reduce(root,current, index):
    for e, i in enumerate(current):
        if len(index) == 4 and i is list:
            rev = index[::-1]
            pos = rev.find(str(e))





def reduce(snail):
    index = ''
    return _reduce(snail, snail, index)




def main():
    with open('input.txt', 'r') as file:
        first = eval(next(file))
        data = file.read().splitlines()

    snail = reduce(first)
    for i in data:
        snail = [snail, eval(i)]
        reduce(snail)




if __name__ == '__main__':
    main()
