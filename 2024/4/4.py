with open("./2024/4/input.txt", "r") as f:
    d = [i.strip() for i in f.readlines()]

pos = dict()
for i in range(len(d)):
    for col in range(len(d[0])):
        pos[i+1j*col] = d[i][col]
dirs = [1, -1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j]
xmas = "MAS"
cnt, cnt2 = 0, 0
center = []
for c in pos:
    for i in dirs:
        for j in range(len(xmas)):
            if c + i*j not in pos or pos[c + i*j] != xmas[j]: break
        else:
            if c-i in pos and pos[c-i] == "X": cnt += 1
            if abs(i) > 1:
                cnt2 += c+i in center
                center.append(c+i)

print(cnt)
print(cnt2)
