if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.read()
    print(data.count('(')-data.count(')'))
    level = 0
    base = 0
    for e,i in enumerate(data,1):
        if i == '(':
            level += 1
        else:
            level -= 1
        if level == -1:
            base = e
            break
    print(e)