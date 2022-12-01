def load_input_file(file_name):
    res = []
    with open(file_name) as file:
        data = file.read().splitlines()
    for i in data:
        cube = []
        line = i.split(' ')
        cube = [1] if line[0] == 'on' else [-1]
        line = line[1].split(',')
        for k in line:
            vals = k[2:].split('..')
            cube.append([int(vals[0]), int(vals[1])])
        res.append(cube)
    return res

def intersect(a, b):
    cube = []
    for i in range(3):
        if a[i][1] < b[i][0] or a[i][0] > b[i][1]:
            return False
        cube.append([max(a[i][0], b[i][0]), min(a[i][1], b[i][1])])
    return cube

def calc_ans(cubes):
    res = 0
    for i in cubes:
        res += i[0]*(i[1][1] - i[1][0] + 1) * (i[2][1] - i[2][0] + 1) * (i[3][1] - i[3][0] + 1)
    return res            

def main():
    data = load_input_file('2021\\22\\input.txt')
    cubes = []
    for cube in data:
        for i in cubes.copy():
            inter = intersect(i[1:], cube[1:])
            if inter:
                cubes.append([-1 if i[0]==1 else 1] + inter)
        if cube[0] == 1:
            cubes.append(cube)
    print(calc_ans(cubes))

if __name__ == '__main__':
    main()