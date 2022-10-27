if __name__ == '__main__':
    with open('day2\input.txt') as file:
        data = file.read().splitlines()
    paper = 0
    ribbon = 0
    for line in data:
        l,w,h = map(int,line.split('x'))
        wrap = [l*w, l*h, w*h]
        paper += 2*sum(wrap)+min(wrap)
        ribb = [l+w, w+h, l+h]
        ribbon += 2*min(ribb) + l*w*h
    print(ribbon)
