def expanded(img, n):
    exp = ['.'] * n
    ximg = [exp.copy()+i+exp.copy() for i in img]
    yexp = ['.'] * len(ximg[0])
    sv = []
    for i in range(n):
        sv.append(yexp.copy())
    sv += ximg
    for i in range(n):
        sv.append(yexp.copy())
    return sv


def blank(img):
    row = ['.'] * len(img[0])
    mat = []
    for i in range(len(img)):
        mat.append(row.copy())
    return mat


def main():
    exp = 400
    ite = 50

    with open('input.txt', 'r') as file:
        algo = next(file).strip()
        next(file)
        raw_image1 = file.read().splitlines()
    image = [list(i) for i in raw_image1]
    org_row = len(image)
    org_len = len(image[0])
    image = expanded(image,exp)
    new_image = blank(image)
    for i in image:
        for j in i:
            print(j,end='')
        print()
    for num in range(ite):
        print(f'algo {num}')
        for row_ind, row in enumerate(image[1:-1],1):
            for pos_ind, pos in enumerate(row[1:-1],1):
                val = ''
                for i in range(3):
                    for j in range(3):
                        cur = image[row_ind-1+i][pos_ind-1+j]
                        if cur == '.':
                            val = val + '0'
                        if cur == '#':
                            val = val + '1'
                char = algo[int(val, 2)]
                new_image[row_ind][pos_ind] = char
        image = new_image
        new_image = blank(image)
    k = exp
    rescale = 100
    for i in image[k-rescale:k+org_row+5]:
        for j in i[k-rescale:k+org_len+5]:
            print(j,end='')
        print()
    n = 0

    for row in image[k-rescale:k+org_row+rescale]:
        for pos in row[k-rescale:k+org_len+rescale]:
            if pos == '#':
                n += 1
    print(n)








if __name__ == '__main__':
    main()
