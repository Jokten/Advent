from math import prod


def read_bits(n, bit):
    sv = ''
    for i in range(n):
        sv += str(next(bit))
    return sv


def read_package(dat):
    stop = 0
    binrep = ''
    while stop == 0:
        bit = read_bits(5, dat)
        if int(bit[0]) == 0:
            stop = 1
        binrep += bit[1:]
    return int(binrep, 2)


def read_header(dat):
    version = int(read_bits(3, dat), 2)
    typeID = int(read_bits(3, dat), 2)
    val = []
    if typeID == 4:
        return read_package(dat)
    else:
        lengthID = int(read_bits(1, dat))
        if lengthID == 1:
            nr_sub = int(read_bits(11, dat), 2)
            for i in range(nr_sub):
                val.append(read_header(dat))

        elif lengthID == 0:
            len_sub = int(read_bits(15, dat), 2)
            dat_samp = read_bits(len_sub, dat)
            samp = iter(dat_samp)

            try:
                while True:
                    val.append(read_header(samp))
            except StopIteration:
                pass
    if len(val) == 1:
        outputs = [sum(val), prod(val), min(val), max(val)]
    else:
        outputs = [sum(val), int(prod(val)), min(val), max(val), 1, int(val[0]>val[1]), int(val[0]<val[1]), int(val[0]==val[1])]
    return outputs[typeID]



def main():
    with open('input.txt', 'r') as file:
        data = file.read()
    binary = bin(int('1'+data, 16))[3:]
    print(str(binary))
    bi = iter(binary)
    print(read_header(bi))


if __name__ == '__main__':
    main()
