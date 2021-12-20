def main():
    with open('input.txt', 'r') as file:
        algo = next(file)+next(file)
        raw_image = file.read().splitlines()
    row = (len(raw_image[0])+4)*'.'
    expanded_image = [row, row]
    [expanded_image.append('..'+i+'..') for i in raw_image]
    expanded_image.append(row)
    expanded_image.append(row)
    image = expanded_image

    new_image = [row]*len(raw_image)
    for row_ind, row in enumerate(image[1:-1]):
        for pos_ind, pos in enumerate(row[1:-1], 1):
            val = ''
            for i in range(3):
                for j in range(3):
                    cur = image[row_ind-1+i][pos_ind-1+j]
                    if cur == '.':
                        val = val + '0'
                    if cur == '#':
                        val = val + '1'




if __name__ == '__main__':
    main()
