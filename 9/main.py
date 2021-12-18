def main():
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
    mat = [[int(j) for j in i] for i in data]
    n = 100
    risk = 0
    for i in range(100):
        for j in range(100):
            val = mat[i][j]
            xmin = max(j-1,0)
            xmax = min(j+2,100)
            ymin = max(i - 1, 0)
            ymax = min(i + 1, 99)
            y = [mat[ymax][j],val,mat[ymin][j]]
            x = mat[i][xmin:xmax]
            if val == min(x) and val != max(x) and val == min(y) and val != max(y):
                print(val,[i,j])
                risk += 1 + val
    print(risk)
if __name__ == '__main__':
    main()